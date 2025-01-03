import sys
import os
import tkinter as tk
from tkinter import messagebox
import win32event
import win32api
import winreg
import win32gui
import win32con
import keyboard
import pystray
from PIL import Image, ImageDraw, ImageFont
import threading
import winshell
from win32com.client import Dispatch

# Global variables
exit_event = threading.Event()
tray = None
mutex = None

def create_mutex():
    """
    Create a global mutex to prevent multiple instances
    """
    global mutex
    mutex = win32event.CreateMutex(None, 1, 'Global\\ThumbnailTogglerMutex')
    if win32api.GetLastError() == 183:  # ERROR_ALREADY_EXISTS
        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning("Cảnh báo", "Script đang được chạy rồi!")
        sys.exit()

def create_startup_shortcut():
    """
    Create a shortcut in the Windows Startup folder
    """
    try:
        script_path = os.path.abspath(sys.argv[0])
        startup_folder = winshell.startup()
        shortcut_path = os.path.join(startup_folder, "ThumbnailToggler.lnk")
        
        shell = Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = script_path
        shortcut.WorkingDirectory = os.path.dirname(script_path)
        shortcut.save()
    except Exception as e:
        print(f"Lỗi tạo startup shortcut: {e}")

def hide_console():
    """
    Hide the console window
    """
    import ctypes
    ctypes.windll.user32.ShowWindow(
        ctypes.windll.kernel32.GetConsoleWindow(), 
        0
    )

def create_icon():
    """
    Create a custom tray icon with 'D' letter
    """
    img = Image.new('RGB', (64, 64), color='white')
    draw = ImageDraw.Draw(img)
    
    letter_font = ImageFont.truetype("arial.ttf", 48)
    draw.text((16, 0), "D", font=letter_font, fill='black')
    
    return img

def toggle_thumbnails():
    """
    Toggle thumbnail view in Windows Explorer
    """
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, 
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", 
            0, 
            winreg.KEY_READ | winreg.KEY_WRITE
        )

        try:
            icons_only, _ = winreg.QueryValueEx(key, "IconsOnly")
        except FileNotFoundError:
            icons_only = 0

        new_value = 0 if icons_only == 1 else 1

        winreg.SetValueEx(key, "IconsOnly", 0, winreg.REG_DWORD, new_value)
        
        winreg.CloseKey(key)

        hwnd = win32gui.GetForegroundWindow()
        win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F5, 0)
        win32gui.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_F5, 0)

    except Exception as e:
        print(f"Lỗi: {e}")

def exit_tray(icon, item):
    """
    Exit the application from system tray
    """
    global exit_event
    exit_event.set()
    icon.stop()
    sys.exit()

def setup_tray():
    """
    Setup system tray icon and menu with author information
    """
    global tray
    icon = create_icon()
    
    menu = (
        pystray.MenuItem('Tác giả: Danh Phan', None, enabled=False),
        pystray.MenuItem('Toggle Thumbnails (Ctrl+R)', toggle_thumbnails),
        pystray.MenuItem('Thoát', exit_tray)
    )
    
    tray = pystray.Icon("ThumbnailToggler", icon, "Thumbnail Toggler", menu)
    tray.run()

def main():
    """
    Main application logic
    """
    # Create mutex to prevent multiple instances
    create_mutex()
    
    # Create startup shortcut
    create_startup_shortcut()
    
    # Hide console window
    hide_console()
    
    # Register hotkey Ctrl+R
    keyboard.add_hotkey('ctrl+r', toggle_thumbnails)
    
    # Run tray icon on separate thread
    tray_thread = threading.Thread(target=setup_tray)
    tray_thread.start()
    
    # Wait for exit event
    exit_event.wait()

if __name__ == "__main__":
    main()