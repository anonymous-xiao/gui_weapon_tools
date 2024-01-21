import wx


class Frame(object):
    def __init__(self, parent, width=1000, height=600):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Sean & Weapon_Tools", pos=wx.DefaultPosition,
                          size=wx.Size(width, height), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
