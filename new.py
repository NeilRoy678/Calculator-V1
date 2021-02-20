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
       self.display = wx.TextCtrl(self, wx.TE_READONLY)
       ms.Add(self.display,0,wx.ALL|wx.EXPAND, 4)
       gs = wx.GridSizer(5,4,4,6)
       button1 = wx.Button(self, label='Cls')
       button2 = wx.Button(self, label='Bck')
       button2 = wx.Button(self, label='Bck')
       button3 = wx.Button(self, label='Close')
       button4 = wx.Button(self, label='7')
       button5 = wx.Button(self, label='8')
       button6 = wx.Button(self, label='9')
       button7 = wx.Button(self, label='/')
       button8 = wx.Button(self, label='4')
       button9 = wx.Button(self, label='5')
       button10 =wx.Button(self, label='6')
       button11 =wx.Button(self, label='*')
       button12 =wx.Button(self, label='1')
       button13 =wx.Button(self, label='2')
       button14 =wx.Button(self, label='3')
       button15 =wx.Button(self, label='-')
       button16 =wx.Button(self, label='0')
       button17 =wx.Button(self, label='.')
       button18 =wx.Button(self, label='=')
       button19 =wx.Button(self, label='+')
       gs.Add(button1,0,wx.EXPAND)
       gs.Add(button2,0,wx.EXPAND)
       gs.Add(wx.StaticText(self),wx.EXPAND)
       gs.Add(button3,0,wx.EXPAND)
       gs.Add(button4,0,wx.EXPAND)
       gs.Add(button5,0,wx.EXPAND)
       gs.Add(button6,0,wx.EXPAND)
       gs.Add(button7,0,wx.EXPAND)
       gs.Add(button8,0,wx.EXPAND)
       gs.Add(button9,0,wx.EXPAND)
       gs.Add(button10,0,wx.EXPAND)
       gs.Add(button11,0,wx.EXPAND)
       gs.Add(button12,0,wx.EXPAND)
       gs.Add(button13,0,wx.EXPAND)
       gs.Add(button14,0,wx.EXPAND)
       gs.Add(button15,0,wx.EXPAND)
       gs.Add(button16,0,wx.EXPAND)
       gs.Add(button17,0,wx.EXPAND)
       gs.Add(button18,0,wx.EXPAND)
       gs.Add(button19,0,wx.EXPAND)
       ms.Add(gs,1,wx.HORIZONTAL|wx.EXPAND|wx.ALL,5)
       self.SetSizer(ms)
       # self.display = wx.TextCtrl(self, style=wx.TE_READONLY)  #THIS ENABLES READONYL TXT BAR
       # ms.Add(self.display,0,wx.EXPAND,border =4 )
       
class frame1(wx.Frame):
    def __init__(self):
        super().__init__(None,title = "CALCULATOR")
        panel = Panel1(self)
        self.Show()

    
if __name__ == '__main__':
    app = wx.App(False)
    frame = frame1()
    app.MainLoop()