from button_click_event import Events
import subprocess

"""
代码审计按钮点击事件
"""


class CodeReviewEvents(Events):
    def __init__(self, eventsName):
        super().__init__(eventsName)

    def switch_case(self, value):
        switcher = {
            'seay_click': self.seay_click,
        }
        return switcher.get(value)

    def seay_click(self, event):
        subprocess.Popen("cd gui_other/seay代码审计工具 && Seay源代码审计系统.exe", shell=True)
