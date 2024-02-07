from button_click_event import Events
import subprocess
from setting import java8_path

"""
监控按钮点击事件
"""


class MonitorEvents(Events):
    def __init__(self, eventsName):
        super().__init__(eventsName)

    def switch_case(self, value):
        switcher = {
            'mysql_monitor_click': self.mysql_monitor_click,
        }
        return switcher.get(value)

    def mysql_monitor_click(self, event):
        subprocess.Popen("cd tools/monitor/mysql_monitor_jar && " + java8_path + ' -jar ' + 'MySQLMonitor-1.1.jar', shell=True)