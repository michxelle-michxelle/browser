




window=tk.Tk()
window.title('Browser')

root.iconbitmap(r"C:\Users\usogv\OneDrive\Desktop\build\icon.ico")
window.geometry('800x450')
webbrowser.open('https://www.google.com')

window.mainloop()


window = create_widget(None, tk.Tk)
window.title('GUI Browser')


tk = Tk()
tk.geometry("800x450")
webview.create_window('Webbrowser', 'https://google.com')
webview.start()








class Widgets(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Simple Web Browser")
        self.widget = QWidget(self)

     
        self.webview = QWebEngineView()
        self.webview.load(QUrl("https://www.google.com/"))
        self.webview.urlChanged.connect(self.url_changed)


        self.back_button = QPushButton("<")
        self.back_button.clicked.connect(self.webview.back)
        self.forward_button = QPushButton(">")
        self.forward_button.clicked.connect(self.webview.forward)
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.webview.reload)


        self.url_text = QLineEdit()

        # Button to load the current page.
        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.url_set)

        self.toplayout = QHBoxLayout()
        self.toplayout.addWidget(self.back_button)
        self.toplayout.addWidget(self.forward_button)
        self.toplayout.addWidget(self.refresh_button)
        self.toplayout.addWidget(self.url_text)
        self.toplayout.addWidget(self.go_button)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.toplayout)
        self.layout.addWidget(self.webview)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def url_changed(self, url):
        """Refresh the address bar"""
        self.url_text.setText(url.toString())

    def url_set(self):
        """Load the new URL"""
        self.webview.setUrl(QUrl(self.url_text.text()))












if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widgets()
    window.show()
    sys.exit(app.exec_())



    main_win = create_main_window()
    initial_urls = sys.argv[1:]
    if not initial_urls:
        initial_urls.append('http://qt.io')
    for url in initial_urls:
        main_win.load_url_in_new_tab(QUrl.fromUserInput(url))
    exit_code = app.exec()
    main_win.write_bookmarks()
    sys.exit(exit_code)


 

directory_table = [
	("ProgramMenuFolder", "TARGETDIR", ""),

	("MyPrpgramMenu", "ProgramMenuFolder", "MYPROG-1| MyProgram"),]



bdist_msi_options = {
	"add_to_path": false,

	"all_users": false,

	"initial_target_dir": r"C:\Users\usogv\OneDrive\Desktop\Start",
	
	"install_icon": r"C:\Users\usogv\OneDrive\Desktop\Start\icon.ico",

	"target_name": r"C:\Users\usogv\OneDrive\Desktop\Start\start.exe",

	"extensions": r"C:\Users\usogv\OneDrive\Desktop\Start\start.exe", }



build_exe_options = {

	'packages':[], 

	'excludes':['tkinter', 'unittest'],

	'include_msvcr': True,

	'zip_include_packages': ['encoding', 'PySide6'],

	'include_files': 

		[ r"C:\Users\usogv\OneDrive\Desktop\Start\icon.ico",

r"C:\Users\usogv\OneDrive\Desktop\Start\autostart.inf", 

r"C:\WINDOWS\system32\DRIVERS\umpass.sys",

r"C:\WINDOWS\System32\DRIVERS\scfilter.sys", 

r"C:\WINDOWS\system32\DRIVERS\UMDF\WUDFUsbccidDriver.dll",

r"C:\WINDOWS\system32\DRIVERS\winusb.sys",

r"C:\WINDOWS\system32\drivers\WUDFRd.sys,"

r"C:\WINDOWS\system32\DRIVERS\UMDF\UsbXhciCompanion.dll",

r"C:\WINDOWS\system32\DRIVERS\USBXHCI.SYS" ,

r"C:\WINDOWS\system32\DRIVERS\usbccgp.sys " ,

r"C:\WINDOWS\system32\DRIVERS\USBHUB3.SYS ",

r"usb4deviceroute.inf_amd64_20da523aab577a9c\Usb4DeviceRouter.sys",

r"usb4hostrouter.inf_amd_d1f4f1b9ed26b447\Usb4HostRouter.sys",

r"C:\Users\usogv\OneDrive\Desktop\smartcard_cert.txt",

r"C:\Users\usogv\OneDrive\Desktop\tagliov70pc.txt", 

r"C:\Users\usogv\Downloads\pkadmin(1)\pkadmin\CA-Root-Certificates\pivkeydeviceca.crl",

r"C:\Users\usogv\Downloads\pkadmin(1)\pkadmin\CA-Root-Certificates\pivkeydeviceca.crt",

r"C:\Users\usogv\Downloads\pkadmin(1)\pkadmin\CA-Root-Certificates\server-ca.crt",

r"C:\Users\usogv\Downloads\pkadmin(1)\pkadmin\CA-Root-Certificates\tagliorootca.crl", 

r"C:\Users\usogv\Downloads\pkadmin(1)\pkadmin\CA-Root-Certificates\tagliorootca.crt",  

r"C:\WINDOWS\system32\DRIVERS\usbccgp.sys " ,

r"C:\WINDOWS\system32\DRIVERS\USBHUB3.SYS ",

r"usb4deviceroute.inf_amd64_20da523aab577a9c\Usb4DeviceRouter.sys",

r"usb4hostrouter.inf_amd_d1f4f1b9ed26b447\Usb4HostRouter.sys",

r"C:\WINDOWS\system32\DRIVERS\MTConfig.sys"

r"C:\WINDOWS\system32\DRIVERS\hidclass.sys",

r"C:\WINDOWS\system32\DRIVERS\hidparse.sys",

r"C:\WINDOWS\system32\DRIVERS\hidusb.sys",

r"C:\WINDOWS\system32\DRIVERS\UcmUcsiAcpiClient.sys"



],
}




import sys

base = 'Win64GUI' if sys.platform=='win64' else None

executable = [

Executable(r"C:\Users\usogv\OneDrive\Desktop\build\build.exe",
base=base,
target_name = r"C:\Users\usogv\OneDrive\Desktop\build\build.exe",
copyright="2025 cxFreeze",
icon=r"C:\Users\usogv\OneDrive\Desktop\Start\icon.ico",
shortcut_name="MyStartBrowser",
shortcut_dir="MyStartBrowser",
)]



cx_Freeze.setup(

name="build.exe",
	version="0.1",
	description="browser",

	options={
	"build_exe": build_exe_options,
	"msi_data": msi_data,
	"bdist_msi": bdist_msi_options,
	"py2exe": {'bundle_files':2, 'compressed': True}},

	executables=[Executables(r"C:\Users\usogv\OneDrive\Desktop\build\build.exe", 
		base=base, 
		targetname="", 
		targetdirectory="")],

	
	
	zipfile=None,
	packages=find_packages(exclude=["tests"]),
	)




block_cipher = None


a = Analysis(
    ['C:\\Users\\usogv\\OneDrive\\Desktop\\Start\\start.py', 'build'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='start',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='start',
)
