import webbrowser
import time
import pyautogui
import platform
import requests
from bs4 import BeautifulSoup
import psutil

# 检测操作系统
is_windows = platform.system() == 'Windows'
is_linux = platform.system() == 'Linux'

if is_windows:
    import pygetwindow as gw  # Windows 上使用 pygetwindow
elif is_linux:
    import subprocess  # Ubuntu 上使用 subprocess 调用 xdotool

# 用于检测网络连接的 URL
bing_url = 'https://www.bing.com'

# 上网认证页面 URL
auth_url = 'https://login.hdu.edu.cn/srun_portal_pc?ac_id=0&theme=pro'

# 检查网络连接的函数
def check_network():
    try:
        response = requests.get(bing_url, timeout=5)
        if response.status_code == 200:
            print("网络正常，已连接到互联网。")
            return True
        else:
            print("网络连接异常。")
            return False
    except (requests.ConnectionError, requests.Timeout):
        print("无法连接到 Bing，可能没有网络连接。")
        return False

# 检查指定浏览器是否运行
def is_browser_running(browser_name):
    # 遍历所有正在运行的进程，查找指定浏览器进程
    for process in psutil.process_iter(['name']):
        if process.info['name'] and browser_name.lower() in process.info['name'].lower():
            return True
    return False

# 调整窗口并模拟点击中间并按 Tab 然后回车（Windows）
def adjust_window_and_input_windows():
    browser_window = None

    # 打印所有窗口标题，确认浏览器窗口名称
    all_titles = gw.getAllTitles()
    for window in all_titles:
        if 'Edge' in window:  # 检查标题中是否包含 'Edge'
            browser_window = gw.getWindowsWithTitle(window)[0]
            break

    if browser_window:
        # 调整窗口大小和位置
        browser_window.resizeTo(1024, 768)
        browser_window.moveTo(100, 100)
        time.sleep(2)  # 等待窗口调整完成

        # 模拟点击网页中间并按 Tab 键，再按回车
        # pyautogui.click(x=512, y=384)  # 假设网页中心为窗口的中心
        time.sleep(1)
        pyautogui.press('tab')  # 按下 Tab 键
        pyautogui.press('enter')  # 按下 Enter 键
    else:
        print("找不到 Microsoft Edge 浏览器窗口，请确保浏览器已经打开。")

# 调整窗口并模拟点击中间并按 Tab 然后回车（Linux）
def adjust_window_and_input_linux():
    # 获取当前活动窗口
    subprocess.run(["xdotool", "search", "--name", "Mozilla Firefox", "windowactivate"])

    # 调整窗口大小和位置
    subprocess.run(["xdotool", "getactivewindow", "windowmove", "100", "100"])
    subprocess.run(["xdotool", "getactivewindow", "windowsize", "1024", "768"])

    # 等待窗口调整完成
    time.sleep(2)

    # 模拟点击网页中间并按 Tab 键，再按回车
    pyautogui.click(x=512, y=384)  # 假设网页中心为窗口的中心
    time.sleep(1)
    pyautogui.press('tab')  # 按下 Tab 键
    pyautogui.press('enter')  # 按下 Enter 键

# 自动打开认证页面并模拟点击操作
def authenticate():
    print(f"访问上网认证页面：{auth_url}")
    webbrowser.open(auth_url)  # 使用默认浏览器打开认证页面

    # 等待页面加载完成
    time.sleep(8)

    # 根据操作系统调整窗口并进行操作
    if is_windows:
        adjust_window_and_input_windows()
    elif is_linux:
        adjust_window_and_input_linux()

# 主函数逻辑
def main():
    while True:
        # 检查网络连接
        if check_network():
            print("网络连接正常，不需要认证。")
        else:
            print("没有检测到网络连接，尝试访问上网认证页面...")

            # 尝试认证
            authenticate()

        # 每隔 10 秒检查一次网络状态
        time.sleep(10)

if __name__ == "__main__":
    main()
