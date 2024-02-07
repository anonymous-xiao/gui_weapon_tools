from button_click_event import Events
import subprocess
from setting import java8_path
import platform
"""
漏洞扫描按钮点击事件
"""
class VulScanEvents(Events):
    def __init__(self, eventsName):
        super().__init__(eventsName)

    def switch_case(self, value):
        switcher = {
            'xray_click': self.xray_click,
            'goby_click': self.goby_click,
            'sqlmap_click': self.sqlmap_click,
            'behinder_click': self.behinder_click
        }
        return switcher.get(value)

    def xray_click(self, event):
        if platform.system() == 'Windows':
            # cmd 形式
            # subprocess.Popen("start cmd /k \"cd tools/xray-all-1.9.11/win_amd64 && xray_windows_amd64.exe\"", shell=True)
            # powershell 形式
            subprocess.Popen("start powershell -NoExit -Command \"cd 'tools/xray-all-1.9.11/win_amd64'; .\\xray_windows_amd64.exe\"", shell=True)

        else:
            subprocess.Popen("cd tools/xray-all-1.9.11/mac_amd64 && xray_linux_amd64", shell=True)


    def goby_click(self, event):
        if platform.system() == 'Windows':
            subprocess.Popen("cd tools\\goby\\goby-win-x64-2.4.7_RD\\goby-win-x64-2.4.7_Red_Team && Goby.exe", shell=True)

        else:
            pass
        # subprocess.Popen("cd tools/xray-all-1.9.11/mac_amd64 && xray_linux_amd64", shell=True)

    def behinder_click(self, event):
        subprocess.Popen("cd gui_webshell/Behinder && " + java8_path + ' -jar ' + 'Behinder.jar', shell=True)
    def sqlmap_click(self, event):
        subprocess.Popen("start cmd /k \"cd tools/sqlmap-1.8 && python sqlmap.py --help\"", shell=True)

