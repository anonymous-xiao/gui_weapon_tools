import wx
from button_click_event import Events


class Button:
    def __init__(self, buttonName):
        self.buttonName = buttonName
        # self.buttonEvents = Events(eventsName)

    def createButton(self, gui_module, index):
        return wx.Button(gui_module.GetStaticBox(), wx.ID_ANY, self.buttonName.split(";")[index], wx.DefaultPosition,
                         wx.DefaultSize, 0)
        # module_sizer.Add(button, 0, wx.ALL, 5)
        # button.Bind(wx.EVT_BUTTON, self.buttonEvents.switch_case(self.buttonEvents().eventName))
