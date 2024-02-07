# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from init_frame import Frame

###########################################################################
## Class jar_management_gui
###########################################################################
from webShell.web_shell import WebShellModule
from webShell.web_shell_button import WebShellButton
from webShell.web_shell_events import WebShellEvents
from codeReview.code_review import CodeReviewModule
from codeReview.code_review_button import CodeReviewButton
from codeReview.code_review_events import CodeReviewEvents
from monitor.monitor import MonitorModule
from monitor.monitor_button import MonitorButton
from monitor.monitor_events import MonitorEvents
from penTest.pen import PenModule
from penTest.pen_button import PenButton
from penTest.pen_events import PenEvents
from vulScan.vul_scan import VulScanModule
from vulScan.vul_scan_button import VulScanButton
from vulScan.vul_scan_events import VulScanEvents


class jar_management_gui(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Sean & Weapon_Tools", pos=wx.DefaultPosition,
                          size=wx.Size(1000, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.gui_all = wx.BoxSizer(wx.VERTICAL)

        # WebShell管理工具
        WebShellModule(u"Webshell管理工具").createModule(self, WebShellButton(u"Godzilla_v3.03;Behinder"),
                                                         WebShellEvents(u"godzilla_click"))
        # 渗透测试管理工具
        PenModule(u"渗透工具").createModule(self, PenButton(u"Burpsuite_pro_v2022.1.1-All"),
                                                    PenEvents(u"burp_suite_click"))


        gui_shouji = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"信息收集"), wx.VERTICAL)

        shouji = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.dirscan = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"Dirscan_v3.0", wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        shouji.Add(self.dirscan, 0, wx.ALL, 5)

        self.webfinder = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"Webfinder_v3.2", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        shouji.Add(self.webfinder, 0, wx.ALL, 5)

        self.fofa = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"Fofa_Viewer_v1.0.8", wx.DefaultPosition,
                              wx.DefaultSize, 0)
        shouji.Add(self.fofa, 0, wx.ALL, 5)

        self.yjdirscan = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"御剑dirscan_v1.1", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        shouji.Add(self.yjdirscan, 0, wx.ALL, 5)

        gui_shouji.Add(shouji, 1, wx.EXPAND, 5)

        self.gui_all.Add(gui_shouji, 0, wx.EXPAND | wx.ALL, 5)

        # 漏洞扫描工具
        VulScanModule(u"漏洞扫描").createModule(self, VulScanButton(u"xray_1.9.11_All;goby_2.4.7_Win;sqlmap_1.8_All"),
                                            VulScanEvents(u"xray_click;goby_click;sqlmap_click"))

        # 渗透测试管理工具
        # PenModule(u"渗透工具").createModule(self, PenButton(u"Burpsuite_pro_v2022.1.1-All"),
        #                                     PenEvents(u"burp_suite_click"))
        #
        # gui_scan = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"漏洞扫描"), wx.VERTICAL)
        #
        #
        #
        # scan = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)
        #
        # self.tdoa = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"通达OA综合利用工具_v1.0", wx.DefaultPosition,
        #                       wx.DefaultSize, 0)
        # scan.Add(self.tdoa, 0, wx.ALL, 5)
        #
        # self.Gr33k = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"Gr33k漏洞利用工具集_py", wx.DefaultPosition,
        #                        wx.DefaultSize, 0)
        # scan.Add(self.Gr33k, 0, wx.ALL, 5)
        #
        # self.Cas = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"Cas反序列化漏洞利用工具_v1.1", wx.DefaultPosition,
        #                      wx.DefaultSize, 0)
        # scan.Add(self.Cas, 0, wx.ALL, 5)
        #
        # self.sj = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"神机_V.19", wx.DefaultPosition, wx.DefaultSize, 0)
        # scan.Add(self.sj, 0, wx.ALL, 5)
        #
        # self.thinkphp = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"ThinkPHP综合利用工具_V2.0", wx.DefaultPosition,
        #                           wx.DefaultSize, 0)
        # scan.Add(self.thinkphp, 0, wx.ALL, 5)
        #
        # self.thinkphp_log = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"ThinkPHP日志分析_v1.2_Beta_win",
        #                               wx.DefaultPosition, wx.DefaultSize, 0)
        # scan.Add(self.thinkphp_log, 0, wx.ALL, 5)
        #
        # self.thinkphp1 = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"Thinkphp漏洞利用工具_v1.2", wx.DefaultPosition,
        #                            wx.DefaultSize, 0)
        # scan.Add(self.thinkphp1, 0, wx.ALL, 5)
        #
        # self.thinkphp2 = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"thinkphp命令执行检测工具", wx.DefaultPosition,
        #                            wx.DefaultSize, 0)
        # scan.Add(self.thinkphp2, 0, wx.ALL, 5)
        #
        # self.weblogic_framework = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"weblogic-framework",
        #                                     wx.DefaultPosition, wx.DefaultSize, 0)
        # scan.Add(self.weblogic_framework, 0, wx.ALL, 5)
        #
        # self.weblogic1 = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"weblogic漏洞利用工具", wx.DefaultPosition,
        #                            wx.DefaultSize, 0)
        # scan.Add(self.weblogic1, 0, wx.ALL, 5)
        #
        # self.edr = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"深X服edr任意用户登陆检测工具", wx.DefaultPosition,
        #                      wx.DefaultSize, 0)
        # scan.Add(self.edr, 0, wx.ALL, 5)
        #
        # self.shiro_attack = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"shiro_attack_2.2", wx.DefaultPosition,
        #                               wx.DefaultSize, 0)
        # scan.Add(self.shiro_attack, 0, wx.ALL, 5)
        #
        # self.ShiroExp = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"ShiroExp_v1.0", wx.DefaultPosition,
        #                           wx.DefaultSize, 0)
        # scan.Add(self.ShiroExp, 0, wx.ALL, 5)
        #
        # self.ShiroExploit = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"ShiroExploit_v2.3", wx.DefaultPosition,
        #                               wx.DefaultSize, 0)
        # scan.Add(self.ShiroExploit, 0, wx.ALL, 5)
        #
        # self.ShiroExploit1 = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"ShiroExploit", wx.DefaultPosition,
        #                                wx.DefaultSize, 0)
        # scan.Add(self.ShiroExploit1, 0, wx.ALL, 5)
        #
        # self.ShiroScan = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"ShiroScan_v1.1", wx.DefaultPosition,
        #                            wx.DefaultSize, 0)
        # scan.Add(self.ShiroScan, 0, wx.ALL, 5)
        #
        # self.ShiroExploit2 = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"ShiroExploit_V2.51", wx.DefaultPosition,
        #                                wx.DefaultSize, 0)
        # scan.Add(self.ShiroExploit2, 0, wx.ALL, 5)
        #
        # self.oracleShell = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"oracleShell_v0.1", wx.DefaultPosition,
        #                              wx.DefaultSize, 0)
        # scan.Add(self.oracleShell, 0, wx.ALL, 5)
        #
        # self.FrameScan = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"FrameScan_GUI_win", wx.DefaultPosition,
        #                            wx.DefaultSize, 0)
        # scan.Add(self.FrameScan, 0, wx.ALL, 5)
        #
        # self.tomcat_password = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"tomcat_password", wx.DefaultPosition,
        #                                  wx.DefaultSize, 0)
        # scan.Add(self.tomcat_password, 0, wx.ALL, 5)
        #
        # self.fastjson = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"fastjson检测工具_win", wx.DefaultPosition,
        #                           wx.DefaultSize, 0)
        # scan.Add(self.fastjson, 0, wx.ALL, 5)
        #
        # self.CVE_2020_10199 = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"CVE-2020-10199", wx.DefaultPosition,
        #                                 wx.DefaultSize, 0)
        # scan.Add(self.CVE_2020_10199, 0, wx.ALL, 5)
        #
        # self.CVE_2019_7238 = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"CVE-2019-7238", wx.DefaultPosition,
        #                                wx.DefaultSize, 0)
        # scan.Add(self.CVE_2019_7238, 0, wx.ALL, 5)
        #
        # self.aliyun_accesskey = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"阿里云accesskey利用工具_V1.2_win",
        #                                   wx.DefaultPosition, wx.DefaultSize, 0)
        # scan.Add(self.aliyun_accesskey, 0, wx.ALL, 5)
        #
        # self.AliyunAkTools = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"AliyunAkTools_win", wx.DefaultPosition,
        #                                wx.DefaultSize, 0)
        # scan.Add(self.AliyunAkTools, 0, wx.ALL, 5)
        #
        # self.mdut = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"MDUT_v2.0.6", wx.DefaultPosition, wx.DefaultSize, 0)
        # scan.Add(self.mdut, 0, wx.ALL, 5)
        #
        # gui_scan.Add(scan, 1, wx.EXPAND, 5)
        #
        # self.gui_all.Add(gui_scan, 0, wx.EXPAND | wx.ALL, 5)

        # 代码审计
        # seayPHP代码审计
        CodeReviewModule(u"代码审计").createModule(self, CodeReviewButton(u"Seay源代码审计系统-Win"),
                                                   CodeReviewEvents(u"seay_click"))

        # 监控
        # mysql监控
        MonitorModule(u"监控").createModule(self, MonitorButton(u"MySQLMonitor-1.1-All"),
                                            MonitorEvents(u"mysql_monitor_click"))

        self.SetSizer(self.gui_all)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.dirscan.Bind(wx.EVT_BUTTON, self.dirscan_click)
        self.webfinder.Bind(wx.EVT_BUTTON, self.webfinder_click)
        self.fofa.Bind(wx.EVT_BUTTON, self.fofa_click)
        self.yjdirscan.Bind(wx.EVT_BUTTON, self.yj_click)
        # self.tdoa.Bind(wx.EVT_BUTTON, self.tdoa_click)
        # self.Gr33k.Bind(wx.EVT_BUTTON, self.gr33k_click)
        # self.Cas.Bind(wx.EVT_BUTTON, self.cas_click)
        # self.sj.Bind(wx.EVT_BUTTON, self.sj_click)
        # self.thinkphp.Bind(wx.EVT_BUTTON, self.thinkphp_click)
        # self.thinkphp_log.Bind(wx.EVT_BUTTON, self.thinkphp_log_click)
        # self.thinkphp1.Bind(wx.EVT_BUTTON, self.thinkphp1_click)
        # self.thinkphp2.Bind(wx.EVT_BUTTON, self.thinkphp2_click)
        # self.weblogic_framework.Bind(wx.EVT_BUTTON, self.weblogic_click)
        # self.weblogic1.Bind(wx.EVT_BUTTON, self.weblogic1_click)
        # self.edr.Bind(wx.EVT_BUTTON, self.edr_click)
        # self.shiro_attack.Bind(wx.EVT_BUTTON, self.shiro_attack_click)
        # self.ShiroExp.Bind(wx.EVT_BUTTON, self.shiroexp_click)
        # self.ShiroExploit.Bind(wx.EVT_BUTTON, self.shiroexploit_click)
        # self.ShiroExploit1.Bind(wx.EVT_BUTTON, self.shiroexploit1_cilck)
        # self.ShiroScan.Bind(wx.EVT_BUTTON, self.shiroscan_click)
        # self.ShiroExploit2.Bind(wx.EVT_BUTTON, self.shiro1_click)
        # self.oracleShell.Bind(wx.EVT_BUTTON, self.oracleshell_click)
        # self.FrameScan.Bind(wx.EVT_BUTTON, self.framescan_click)
        # self.tomcat_password.Bind(wx.EVT_BUTTON, self.tomcat_password_click)
        # self.fastjson.Bind(wx.EVT_BUTTON, self.fastjson_cilck)
        # self.CVE_2020_10199.Bind(wx.EVT_BUTTON, self.cve_2020_10199_click)
        # self.CVE_2019_7238.Bind(wx.EVT_BUTTON, self.cve_2019_7238_click)
        # self.aliyun_accesskey.Bind(wx.EVT_BUTTON, self.aliyun_accesskey_click)
        # self.AliyunAkTools.Bind(wx.EVT_BUTTON, self.aliyunakyools_click)
        # self.mdut.Bind(wx.EVT_BUTTON, self.mdut_click)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    # def godzilla_click( self, event ):
    # 	event.Skip()

    def behinder_click(self, event):
        event.Skip()

    def burp_suite_click(self, event):
        event.Skip()

    def cs_click(self, event):
        event.Skip()

    def dirscan_click(self, event):
        event.Skip()

    def webfinder_click(self, event):
        event.Skip()

    def fofa_click(self, event):
        event.Skip()

    def yj_click(self, event):
        event.Skip()

    def tdoa_click(self, event):
        event.Skip()

    def gr33k_click(self, event):
        event.Skip()

    def cas_click(self, event):
        event.Skip()

    def sj_click(self, event):
        event.Skip()

    def thinkphp_click(self, event):
        event.Skip()

    def thinkphp_log_click(self, event):
        event.Skip()

    def thinkphp1_click(self, event):
        event.Skip()

    def thinkphp2_click(self, event):
        event.Skip()

    def weblogic_click(self, event):
        event.Skip()

    def weblogic1_click(self, event):
        event.Skip()

    def edr_click(self, event):
        event.Skip()

    def shiro_attack_click(self, event):
        event.Skip()

    def shiroexp_click(self, event):
        event.Skip()

    def shiroexploit_click(self, event):
        event.Skip()

    def shiroexploit1_cilck(self, event):
        event.Skip()

    def shiroscan_click(self, event):
        event.Skip()

    def shiro1_click(self, event):
        event.Skip()

    def oracleshell_click(self, event):
        event.Skip()

    def framescan_click(self, event):
        event.Skip()

    def tomcat_password_click(self, event):
        event.Skip()

    def fastjson_cilck(self, event):
        event.Skip()

    def cve_2020_10199_click(self, event):
        event.Skip()

    def cve_2019_7238_click(self, event):
        event.Skip()

    def aliyun_accesskey_click(self, event):
        event.Skip()

    def aliyunakyools_click(self, event):
        event.Skip()

    def mdut_click(self, event):
        event.Skip()

    def seay_click(self, event):
        event.Skip()
