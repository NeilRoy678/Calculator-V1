'''CALCULATOR PROGRAMMER V1.0
    AUTHOR:NEIL ROY
    START DATE : 19th feb 2021
    END DATE : 
'''
import wx
class Panel1(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)
        ms = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_READONLY)  #THIS ENABLES READONYL TXT BAR
        ms.Add(self.display,0,wx.EXPAND,border =4 )
        gs = wx.GridSizer(5,4,5,5)
        gs.AddMany([(wx.Button(self, label='Cls'), 0, wx.EXPAND),
            (wx.Button(self, label='Bck'), 0, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (wx.Button(self, label='Close'), 0, wx.EXPAND),
            (wx.Button(self, label='7'), 0, wx.EXPAND),
            (wx.Button(self, label='8'), 0, wx.EXPAND),
            (wx.Button(self, label='9'), 0, wx.EXPAND),
            (wx.Button(self, label='/'), 0, wx.EXPAND),
            (wx.Button(self, label='4'), 0, wx.EXPAND),
            (wx.Button(self, label='5'), 0, wx.EXPAND),
            (wx.Button(self, label='6'), 0, wx.EXPAND),
            (wx.Button(self, label='*'), 0, wx.EXPAND),
            (wx.Button(self, label='1'), 0, wx.EXPAND),
            (wx.Button(self, label='2'), 0, wx.EXPAND),
            (wx.Button(self, label='3'), 0, wx.EXPAND),
            (wx.Button(self, label='-'), 0, wx.EXPAND),
            (wx.Button(self, label='0'), 0, wx.EXPAND),
            (wx.Button(self, label='.'), 0, wx.EXPAND),
            (wx.Button(self, label='='), 0, wx.EXPAND),
            (wx.Button(self, label='+'), 0, wx.EXPAND)])
        ms.Add(gs,1,wx.EXPAND)
        self.SetSizer(ms)
class frame1(wx.Frame):
    def __init__(self):
        super().__init__(None,title = "CALCULATOR")
        panel = Panel1(self)
        self.Show()
        
if __name__ == '__main__':
    app = wx.App(False)
    frame = frame1()
    app.MainLoop()