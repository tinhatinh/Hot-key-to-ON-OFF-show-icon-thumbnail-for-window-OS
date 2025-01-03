General Description:

This is a small Windows application written in Python that allows users to easily toggle the thumbnail view in Windows Explorer. The application runs from a system tray icon and can be controlled through a hotkey or the context menu. It also supports automatic startup when the computer boots up and ensures that only one instance of the application is running at a time.
Main Features:

    Prevents Multiple Instances:
        Uses a mutex to ensure that only one instance of the application is running at any given time. If the user tries to run the application again, a warning will be displayed, and the app will exit automatically.

    Create Startup Shortcut:
        Creates a shortcut in the Windows Startup folder so the application starts automatically when the computer boots up.

    Hide Console Window:
        Hides the console window upon startup, so users do not see the command-line window running in the background.

    System Tray Icon:
        Displays a custom icon in the system tray with the letter "D". The icon allows the user to open a context menu with the following options:
            Toggle Thumbnails (Ctrl+R): Toggles the thumbnail view in Windows Explorer.
            Author: Displays author information.
            Exit: Closes the application.

    Hotkey Support:
        Users can press Ctrl+R to toggle the thumbnail view without interacting with the system tray icon.

    Windows Explorer Refresh:
        When the thumbnail view is toggled, the app sends an F5 keystroke to the active window to refresh Windows Explorer immediately, applying the change.

How It Works:

    Initialize Mutex:
        The program checks if an instance of the application is already running. If it is, the app will exit and show a warning message.

    Create Startup Shortcut:
        It creates a shortcut for the app in the Windows Startup folder, ensuring the app runs automatically when the computer starts up.

    Hide Console Window:
        The application hides the console window so that the user only sees the system tray icon.

    Register Hotkey:
        The Ctrl+R hotkey is registered so that users can toggle the thumbnail view quickly without interacting with the tray icon.

    Display System Tray Icon:
        The tray icon allows the user to access options like toggling thumbnails, viewing author information, or exiting the application.

    Toggle Thumbnail View:
        When the user selects the toggle thumbnail option, the application modifies a registry value to switch between displaying icons only or showing thumbnails in Windows Explorer.

Libraries Used:

    tkinter: Used to display the warning message when multiple instances of the app are detected.
    pystray: Creates the tray icon and menu in the system tray.
    keyboard: Registers the hotkey Ctrl+R for toggling thumbnails.
    win32api, win32event, win32con, winreg, win32gui: These are used to interact with Windows system components like the registry, window handling, and system events.
    Pillow (PIL): Used to create and draw the icon for the system tray.
    winshell and win32com: Used to create a shortcut in the Windows Startup folder.

Usage Notes:

    You will need to install external libraries like pystray, Pillow, keyboard, and pywin32.
    If you do not want the app to start automatically, you can disable the startup shortcut creation feature.

This application is particularly useful for users who frequently switch between different thumbnail views in Windows Explorer without having to open the Explorer window or perform manual actions.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Mô tả chung:

Đây là một ứng dụng nhỏ cho Windows được viết bằng Python, cho phép người dùng dễ dàng chuyển đổi chế độ xem thumbnail (hình thu nhỏ) trong Windows Explorer. Ứng dụng này hoạt động từ một biểu tượng trong khay hệ thống (system tray) và có thể được điều khiển thông qua phím tắt hoặc menu ngữ cảnh. Nó cũng hỗ trợ khởi động tự động khi máy tính bật và đảm bảo rằng chỉ có một phiên bản duy nhất của ứng dụng đang chạy.
Các tính năng chính:

    Ngăn ngừa chạy nhiều phiên bản:
        Sử dụng mutex để đảm bảo chỉ có một phiên bản của ứng dụng đang chạy tại một thời điểm. Nếu người dùng cố gắng chạy ứng dụng lần thứ hai, một cảnh báo sẽ hiển thị và ứng dụng sẽ tự động thoát.

    Tạo shortcut trong Startup:
        Tạo một shortcut trong thư mục Startup của Windows để tự động khởi động ứng dụng khi máy tính bật.

    Ẩn cửa sổ console:
        Ẩn cửa sổ console khi ứng dụng khởi động, giúp người dùng không thấy cửa sổ dòng lệnh trong khi ứng dụng chạy nền.

    Biểu tượng trong khay hệ thống:
        Hiển thị một biểu tượng trong khay hệ thống với chữ "D". Biểu tượng này cho phép người dùng mở menu ngữ cảnh với các tùy chọn:
            Toggle Thumbnails (Ctrl+R): Chuyển đổi chế độ xem thumbnail trong Windows Explorer.
            Tác giả: Thông tin tác giả.
            Thoát: Đóng ứng dụng.

    Phím tắt (Hotkey):
        Người dùng có thể nhấn Ctrl+R để chuyển đổi chế độ xem thumbnail mà không cần mở menu.

    Cập nhật Windows Explorer:
        Khi thay đổi chế độ xem thumbnail, ứng dụng gửi lệnh F5 đến cửa sổ đang hiển thị để làm mới Windows Explorer, giúp thay đổi có hiệu lực ngay lập tức.

Các bước hoạt động:

    Khởi tạo Mutex:
        Kiểm tra xem ứng dụng có đang chạy hay không. Nếu có, ứng dụng sẽ thoát và hiển thị một thông báo cảnh báo.

    Tạo Shortcut khởi động:
        Tạo một shortcut cho ứng dụng trong thư mục Startup của Windows, đảm bảo ứng dụng sẽ tự động chạy mỗi khi máy tính khởi động lại.

    Ẩn Console Window:
        Ứng dụng sẽ ẩn cửa sổ console để không làm gián đoạn giao diện người dùng.

    Khai báo phím tắt (Hotkey):
        Đăng ký phím tắt Ctrl+R để người dùng có thể chuyển đổi chế độ xem thumbnail mà không cần tương tác với biểu tượng trong khay hệ thống.

    Hiển thị Biểu tượng trong Khay hệ thống:
        Biểu tượng này cho phép người dùng truy cập các chức năng như chuyển đổi chế độ xem thumbnail, thông tin tác giả, và thoát khỏi ứng dụng.

    Chuyển đổi chế độ xem thumbnail:
        Khi người dùng chọn tùy chọn chuyển đổi thumbnail, ứng dụng sẽ thay đổi giá trị trong registry của Windows, giúp chuyển đổi giữa chế độ xem icon thông thường và chế độ chỉ hiển thị icon mà không có thumbnail.

Các thư viện sử dụng:

    tkinter: Được sử dụng để hiển thị thông báo cảnh báo khi có nhiều phiên bản của ứng dụng.
    pystray: Tạo biểu tượng và menu trong khay hệ thống.
    keyboard: Để đăng ký phím tắt (hotkey) Ctrl+R.
    win32api, win32event, win32con, winreg, win32gui: Dùng để thao tác với các thành phần hệ thống Windows như registry, cửa sổ và sự kiện.
    PIL (Pillow): Dùng để tạo và vẽ biểu tượng cho khay hệ thống.
    winshell và win32com: Dùng để tạo shortcut trong thư mục Startup.

Lưu ý khi sử dụng:

    Cần cài đặt các thư viện ngoài như pystray, Pillow, keyboard, và pywin32.
    Nếu không muốn ứng dụng khởi động tự động, bạn có thể vô hiệu hóa chức năng tạo shortcut trong Startup.

Ứng dụng này rất hữu ích cho những người muốn thay đổi nhanh chế độ xem thumbnail trong Windows mà không cần mở cửa sổ Explorer hoặc thực hiện thao tác thủ công.
