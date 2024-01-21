import wx
from init_button import Button
from button_click_event import Events


class Module:
    def __init__(self, moduleName):
        self.moduleName = moduleName
        # self.button = Button(buttonName, eventsName)

    def createModule(self, parent, buttonClass, eventsClass):
        gui_module = wx.StaticBoxSizer(wx.StaticBox(parent, wx.ID_ANY, self.moduleName), wx.VERTICAL)
        module_sizer = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)
        if len(buttonClass.buttonName.split(";")) > 0:
            num = len(buttonClass.buttonName.split(";"))
            for index in range(num):
                button = buttonClass.createButton(gui_module, index)
                try:
                    button.Bind(wx.EVT_BUTTON, eventsClass.switch_case(eventsClass.eventsName.split(";")[index]))
                except IndexError:
                    print("【"+buttonClass.buttonName.split(";")[index]+"】按钮点击事件遗漏！")
                module_sizer.Add(button, 0, wx.ALL, 5)
        gui_module.Add(module_sizer, 1, wx.EXPAND, 5)
        parent.gui_all.Add(gui_module, 0, wx.EXPAND | wx.ALL, 5)
