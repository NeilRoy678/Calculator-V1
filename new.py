'''CALCULATOR PROGRAMMER V1.0
    AUTHOR:NEIL ROY
    START DATE : 19th Feb 2021
    Break : 20th Feb 2021
    END DATE : 
'''
import wx
import operator 
ops = {"+" : operator.add,
       "-" : operator.sub ,
       "*" : operator.mul, 
       "/" : operator.truediv,
       }
class Panel1(wx.Panel):
    def __init__(self,parent):
       super().__init__(parent) 
       ms = wx.BoxSizer(wx.VERTICAL)
       self.display = wx.TextCtrl(self, wx.TE_READONLY)
       ms.Add(self.display,0,wx.ALL|wx.EXPAND, 4)
       gs = wx.GridSizer(5,4,4,6)
       button1 = wx.Button(self, label='Cls')
       button1.Bind(wx.EVT_BUTTON, self.on_button1)
       button2 = wx.Button(self, label='Bck')
       button2.Bind(wx.EVT_BUTTON, self.on_button2)
       button3 = wx.Button(self, label='Close')
       button3.Bind(wx.EVT_BUTTON, self.on_button3)
       button4 = wx.Button(self, label='7')
       button4.Bind(wx.EVT_BUTTON, self.on_button4)
       button5 = wx.Button(self, label='8')
       button5.Bind(wx.EVT_BUTTON, self.on_button5)
       button6 = wx.Button(self, label='9')
       button6.Bind(wx.EVT_BUTTON, self.on_button6)
       button7 = wx.Button(self, label='/')
       button7.Bind(wx.EVT_BUTTON, self.on_button7)
       button8 = wx.Button(self, label='4')
       button8.Bind(wx.EVT_BUTTON, self.on_button8)
       button9 = wx.Button(self, label='5')
       button9.Bind(wx.EVT_BUTTON, self.on_button9)
       button10 =wx.Button(self, label='6')
       button10.Bind(wx.EVT_BUTTON, self.on_button10)
       button11 =wx.Button(self, label='*')
       button11.Bind(wx.EVT_BUTTON, self.on_button11)
       button12 =wx.Button(self, label='1')
       button12.Bind(wx.EVT_BUTTON, self.on_button12)
       button13 =wx.Button(self, label='2')
       button13.Bind(wx.EVT_BUTTON, self.on_button13)
       button14 =wx.Button(self, label='3')
       button14.Bind(wx.EVT_BUTTON, self.on_button14)
       button15 =wx.Button(self, label='-')
       button15.Bind(wx.EVT_BUTTON, self.on_button15)
       button16 =wx.Button(self, label='0')
       button16.Bind(wx.EVT_BUTTON, self.on_button16)
       button17 =wx.Button(self, label='.')
       button17.Bind(wx.EVT_BUTTON, self.on_button17)
       button18 =wx.Button(self, label='=')
       button18.Bind(wx.EVT_BUTTON, self.on_button18)
       button19 =wx.Button(self, label='+')
       button19.Bind(wx.EVT_BUTTON, self.on_button19)
       gs.Add(button1,0,wx.EXPAND)
       gs.Add(button2,0,wx.EXPAND)
       gs.Add(wx.StaticText(self,label =""),wx.EXPAND)
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
    def on_button1(self,event):
        with open("calc.txt","r+") as file_handler:
            file_handler.truncate(0)
            wx.StaticText(self.display,label ="                       ")
    
    def on_button2(self,event):
         print("BUTTON 2")
         
    def on_button3(self,event):
         print("BUTTON 3")
    
    def on_button4(self,event):
        with open("calc.txt",'a') as file_handler:
            file_handler.write('7')
            file_handler.close()
        with open("calc.txt",'r') as file_handler: 
             file = file_handler.read()
             wx.StaticText(self.display,label = file ,style = wx.ALIGN_RIGHT)
             file_handler.close()
        
    def on_button5(self,event):
        with open("calc.txt",'a') as file_handler:
            file_handler.write('8')
            file_handler.close() 
        with open("calc.txt",'r') as file_handler: 
             file = file_handler.read()
             wx.StaticText(self.display,label = file ,style = wx.ALIGN_RIGHT)
             file_handler.close()
         
    def on_button6(self,event):
         with open("calc.txt",'a') as file_handler:
            file_handler.write('9')
            file_handler.close()
         with open("calc.txt",'r') as file_handler: 
             file = file_handler.read()
             wx.StaticText(self.display,label = file ,style = wx.ALIGN_RIGHT)
             file_handler.close()
    def on_button7(self,event):
         with open("calc.txt",'a') as file_handler:
            file_handler.write('/')
            file_handler.close()
         with open("calc.txt",'r') as file_handler: 
             file = file_handler.read()
             wx.StaticText(self.display,label = file ,style = wx.ALIGN_RIGHT)
             file_handler.close()
    
    def on_button8(self,event):
        with open("calc.txt",'a') as file_handler:
            file_handler.write('4')
            file_handler.close()
        with open("calc.txt",'r') as file_handler: 
             file = file_handler.read()
             wx.StaticText(self.display,label = file ,style = wx.ALIGN_RIGHT)
             file_handler.close()
    def on_button9(self,event):
        with open("calc.txt",'a') as file_handler:
            file_handler.write('5')
            file_handler.close()
        with open("calc.txt",'r') as file_handler: 
             file = file_handler.read()
             wx.StaticText(self.display,label = file ,style = wx.ALIGN_RIGHT)
             file_handler.close()
    def on_button10(self,event):
        with open("calc.txt",'a') as file_handler:
            file_handler.write('6')
            file_handler.close()
        with open("calc.txt",'r') as file_handler: 
             file = file_handler.read()
             wx.StaticText(self.display,label = file ,style = wx.ALIGN_RIGHT)
             file_handler.close()
    def on_button11(self,event):
        with open("calc.txt",'a') as file_handler:
            file_handler.write('*')
            file_handler.close()
        with open("calc.txt",'r') as file_handler: 
             file = file_handler.read()
             wx.StaticText(self.display,label = file ,style = wx.ALIGN_RIGHT)
             file_handler.close()
    
    def on_button12(self,event):
        with open("calc.txt",'a') as file_handler:
            file_handler.write('1')
            file_handler.close()
        with open("calc.txt",'r') as file_handler: 
             file = file_handler.read()
             wx.StaticText(self.display,label = file ,style = wx.ALIGN_RIGHT)
             file_handler.close()
    def on_button13(self,event):
        with open("calc.txt",'a') as file_handler:
            file_handler.write('2')
            file_handler.close()
        with open("calc.txt",'r') as file_handler: 
             file = file_handler.read()
             wx.StaticText(self.display,label = file ,style = wx.ALIGN_RIGHT)
             file_handler.close()
    def on_button14(self,event):
        with open("calc.txt",'a') as file_handler:
            file_handler.write('3')
            file_handler.close()
        with open("calc.txt",'r') as file_handler: 
             file = file_handler.read()
             wx.StaticText(self.display,label = file ,style = wx.ALIGN_RIGHT)
             file_handler.close()
    def on_button15(self,event):
        with open("calc.txt",'a') as file_handler:
            file_handler.write('-')
            file_handler.close()
        with open("calc.txt",'r') as file_handler: 
             file = file_handler.read()
             wx.StaticText(self.display,label = file ,style = wx.ALIGN_RIGHT)
             file_handler.close()
    
    def on_button16(self,event):
        with open("calc.txt",'a') as file_handler:
            file_handler.write('0')
            file_handler.close()
        with open("calc.txt",'r') as file_handler: 
             file = file_handler.read()
             wx.StaticText(self.display,label = file ,style = wx.ALIGN_RIGHT)
             file_handler.close()
    
    def on_button17(self,event):
         print("BUTTON 2")
         
    def on_button18(self,event):
         with open("calc.txt", "rt") as file_handler:
             file = file_handler.read()
             for i in range(len(file)):
                 if(file[i] == '+' or file[i] == '-' or file[i] =='*' or file[i] =='/'):
                     wx.StaticText(self.display,label = "                                                        " ,style = wx.ALIGN_RIGHT)
                     wx.StaticText(self.display,label = str(ops[file[i]]  (int(file[0:i]),int(file[i+1:len(file)]))))
    #+
    def on_button19(self,event):
        with open("calc.txt",'a') as file_handler:
            file_handler.write('+')
            file_handler.close()
        with open("calc.txt",'r') as file_handler: 
             file = file_handler.read()
             wx.StaticText(self.display,label = file ,style = wx.ALIGN_RIGHT)
             file_handler.close()
        
       # self.display = wx.TextCtrl(self, style=wx.TE_READONLY)  #THIS ENABLES READONYL TXT BAR
       # ms.Add(self.display,0,wx.EXPAND,border =4 )
       
class frame1(wx.Frame):
    def __init__(self):
        super().__init__(None,title = "CALCULATOR V1.0")
        panel = Panel1(self)
        self.Show()

    
if __name__ == '__main__':
    app = wx.App(False)
    frame = frame1()
    app.MainLoop()