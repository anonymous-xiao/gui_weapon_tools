from button_click_event import Events
import subprocess
from setting import java8_path


class WebShellEvents(Events):
    def __init__(self, eventsName):
        super().__init__(eventsName)

    def switch_case(self, value):
        switcher = {
            'godzilla_click': self.godzilla_click,
            'behinder_click': self.behinder_click
        }
        return switcher.get(value)

    def godzilla_click(self, event):
        subprocess.Popen("cd gui_other/Godzilla && " + java8_path + ' -jar ' + 'Godzilla.jar', shell=True)
    def behinder_click(self, event):
        subprocess.Popen("cd gui_webshell/Behinder && " + java8_path + ' -jar ' + 'Behinder.jar', shell=True)

