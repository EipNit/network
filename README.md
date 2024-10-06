# Network Authentication Script

This Python script automates the process of network authentication using a browser. It checks the network status, automatically opens the authentication page if the network is disconnected, and simulates the user interaction required for authentication. The script is compatible with both Windows and Linux operating systems.

## Features

- **Network Connection Check**: Regularly checks if the internet connection is active.
- **Automatic Browser Interaction**: Opens the authentication page in the default browser and simulates necessary user interactions to authenticate the network.
- **Cross-Platform Support**: Works on both Windows and Linux operating systems.
- **Customizable**: Can be modified to work with different authentication URLs or browsers.

## Prerequisites

- Python 3.x
- Necessary Python packages (`requests`, `bs4`, `pyautogui`, `psutil`).
- Required system utilities for Linux (`xdotool`).
- Microsoft Edge browser (for Windows) or Mozilla Firefox (for Linux).

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

    Create a `requirements.txt` file with the following content:

    ```plaintext
    requests
    beautifulsoup4
    pyautogui
    psutil
    pygetwindow  # Required for Windows
    ```

3. For Linux users, install `xdotool`:

    ```bash
    sudo apt-get install xdotool
    ```

## Usage

1. Open a terminal and navigate to the directory containing `network.py`.

2. Run the script:

    ```bash
    python network.py
    ```

3. The script will continuously check your network connection and automatically open the authentication page if the connection is lost. It will then attempt to interact with the page to complete the authentication process.

### Script Breakdown

- **check_network()**: Checks if there is an active network connection by sending a request to Bing.
- **is_browser_running(browser_name)**: Checks if the specified browser (e.g., Edge or Firefox) is running.
- **adjust_window_and_input_windows()**: Adjusts the browser window and simulates user interaction on Windows.
- **adjust_window_and_input_linux()**: Adjusts the browser window and simulates user interaction on Linux.
- **authenticate()**: Opens the network authentication page in the default browser and simulates interaction based on the operating system.
- **main()**: Main function that continuously checks network status and attempts authentication if needed.

## Customization

1. **Authentication URL**: Modify the `auth_url` variable in the script to point to your network's authentication page:

    ```python
    auth_url = 'https://login.hdu.edu.cn/srun_portal_pc?ac_id=0&theme=pro'
    ```

2. **Browser Window Adjustment**: The script uses specific window titles (`'Edge'` for Windows and `'Mozilla Firefox'` for Linux) to identify and manipulate the browser. Adjust these to match your system's browser settings.

3. **Network Check Interval**: Modify the time interval for checking network status in the `main()` function:

    ```python
    time.sleep(10)  # Checks every 10 seconds
    ```

4. **Browser Automation**: The script currently uses `pyautogui` for simulating keyboard presses (`tab` and `enter`). Adjust these commands based on the requirements of your network's authentication page.

## Troubleshooting

- **Browser Window Not Found**: Ensure that the browser window title matches the one specified in the script (`'Edge'` for Windows or `'Mozilla Firefox'` for Linux).
- **Dependencies**: Make sure all required Python packages and Linux utilities (`xdotool`) are installed.
- **Permissions**: On Linux, the script may need appropriate permissions to control the browser window using `xdotool`.

## Limitations

- The script uses hardcoded positions and window titles for browser automation. Changes to the authentication page's layout or the browser window titles might require modifications to the script.
- Only supports Microsoft Edge on Windows and Mozilla Firefox on Linux by default. To use a different browser, the script must be modified.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or report an issue.

## Contact

For questions or support, please contact [yourname](mailto:yourname@example.com).

