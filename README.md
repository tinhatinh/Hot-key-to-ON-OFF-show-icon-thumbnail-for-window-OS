
# ThumbnailToggler

## General Description

ThumbnailToggler is a small Windows application written in Python that allows users to toggle the thumbnail view in Windows Explorer. The app runs from a system tray icon and can be controlled via a hotkey or the context menu. It also supports automatic startup and ensures only one instance of the application is running at a time.

---

## Installation Steps

### Step 1: Download the .zip File
Download the .zip file containing the application.

### Step 2: Extract the .zip File
Once the file is downloaded, extract the .zip file to any folder on your computer.

### Step 3: Run the .exe File
In the extracted folder, locate and double-click the .exe file (e.g., `ThumbnailToggler.exe`) to run the application. The app will start and display an icon in the system tray.

### Step 4: Disable Startup in Task Manager (Optional)
To prevent the app from starting automatically when Windows boots up:
1. Press `Ctrl + Shift + Esc` to open Task Manager.
2. Go to the `Startup` tab.
3. Find `ThumbnailToggler` in the list.
4. Right-click the app and select `Disable` to prevent automatic startup.

---

## Main Features

- **Prevent Multiple Instances:**  
  Uses a mutex to ensure only one instance of the application runs at any given time. If the app is already running, a warning is shown, and the new instance exits automatically.

- **Create Startup Shortcut:**  
  Creates a shortcut in the Windows Startup folder to launch the app automatically when the computer boots up.

- **Hide Console Window:**  
  The console window is hidden upon startup, so users only see the system tray icon.

- **System Tray Icon:**  
  Displays a custom icon in the system tray with the letter "D." The icon allows the user to access the following options via a context menu:
  - **Toggle Thumbnails (Ctrl+R):** Toggles the thumbnail view in Windows Explorer.
  - **Author:** Displays author information.
  - **Exit:** Closes the application.

- **Hotkey Support:**  
  Users can press `Ctrl+R` to toggle the thumbnail view without interacting with the system tray icon.

- **Windows Explorer Refresh:**  
  The app sends an F5 keystroke to refresh Windows Explorer immediately after toggling the thumbnail view, applying the change instantly.

---

## How It Works

1. **Initialize Mutex:**  
   The app checks if it's already running. If so, it exits and shows a warning.

2. **Create Startup Shortcut:**  
   A shortcut is created in the Windows Startup folder to ensure the app runs on startup.

3. **Hide Console Window:**  
   The console window is hidden so only the system tray icon is visible.

4. **Register Hotkey:**  
   The `Ctrl+R` hotkey is registered to toggle the thumbnail view.

5. **Display System Tray Icon:**  
   The tray icon provides options like toggling thumbnails, viewing author information, or exiting the app.

6. **Toggle Thumbnail View:**  
   Selecting the "Toggle Thumbnails" option modifies a registry value to switch between displaying icons only or showing thumbnails in Windows Explorer.

---

## Libraries Used

- **tkinter:** Displays warning messages when multiple instances of the app are detected.
- **pystray:** Creates the system tray icon and menu.
- **keyboard:** Registers the `Ctrl+R` hotkey for toggling thumbnails.
- **win32api, win32event, win32con, winreg, win32gui:** Interacts with Windows system components like the registry, window handling, and system events.
- **Pillow (PIL):** Creates and draws the system tray icon.
- **winshell & win32com:** Creates a shortcut in the Windows Startup folder.

---

## Usage Notes

- You will need to install external libraries such as pystray, Pillow, keyboard, and pywin32.
- To disable automatic startup, you can opt-out of creating the Startup shortcut during the installation.

This application is perfect for users who want to quickly toggle thumbnail views in Windows Explorer without manually adjusting settings or opening the Explorer window.

--- 
