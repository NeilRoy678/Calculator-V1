'''CALCULATOR PROGRAMMER V1.0
    AUTHOR:NEIL ROY
<<<<<<< HEAD
    START DATE : 19th feb 2021
    END DATE :
  '''
=======
    START DATE : 19th Feb 2021
    Break : 20th Feb 2021
    END DATE : 
'''
>>>>>>> calc
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
       self.display = wx.TextCtrl(self, wx.TE_RIGHT)

       ms.Add(self.display,0,wx.ALL|wx.EXPAND, 4)
       gs = wx.GridSizer(5,4,4,6)
       self.button1 = wx.Button(self, label='Cls')
       self.button1.Bind(wx.EVT_BUTTON, self.on_button1)
       self.button2 = wx.Button(self, label='Bck')
       self.button2.Bind(wx.EVT_BUTTON, self.on_button2)
       self.button3 = wx.Button(self, label='Close')
       self.button3.Bind(wx.EVT_BUTTON, self.on_button3)
       self.button4 = wx.Button(self, label='7')
       self.button4.Bind(wx.EVT_BUTTON, self.on_button4)
       self.button5 = wx.Button(self, label='8')
       self.button5.Bind(wx.EVT_BUTTON, self.on_button5)
       self.button6 = wx.Button(self, label='9')
       self.button6.Bind(wx.EVT_BUTTON, self.on_button6)
       self.button7 = wx.Button(self, label='/')
       self.button7.Bind(wx.EVT_BUTTON, self.on_button7)
       self.button8 = wx.Button(self, label='4')
       self.button8.Bind(wx.EVT_BUTTON, self.on_button8)
       self.button9 = wx.Button(self, label='5')
       self.button9.Bind(wx.EVT_BUTTON, self.on_button9)
       self.button10 =wx.Button(self, label='6')
       self.button10.Bind(wx.EVT_BUTTON, self.on_button10)
       self.button11 =wx.Button(self, label='*')
       self.button11.Bind(wx.EVT_BUTTON, self.on_button11)
       self.button12 =wx.Button(self, label='1')
       self.button12.Bind(wx.EVT_BUTTON, self.on_button12)
       self.button13 =wx.Button(self, label='2')
       self.button13.Bind(wx.EVT_BUTTON, self.on_button13)
       self.button14 =wx.Button(self, label='3')
       self.button14.Bind(wx.EVT_BUTTON, self.on_button14)
       self.button15 =wx.Button(self, label='-')
       self.button15.Bind(wx.EVT_BUTTON, self.on_button15)
       self.button16 =wx.Button(self, label='0')
       self.button16.Bind(wx.EVT_BUTTON, self.on_button16)
       self.button17 =wx.Button(self, label='.')
       self.button17.Bind(wx.EVT_BUTTON, self.on_button17)
       self.button18 =wx.Button(self, label='=')
       self.button18.Bind(wx.EVT_BUTTON, self.on_button18)
       self.button19 =wx.Button(self, label='+')
       self.button19.Bind(wx.EVT_BUTTON, self.on_button19)
       gs.Add(self.button1,0,wx.EXPAND)
       gs.Add(self.button2,0,wx.EXPAND)
       gs.Add(wx.StaticText(self,label =""),wx.EXPAND)
       gs.Add(self.button3,0,wx.EXPAND)
       gs.Add(self.button4,0,wx.EXPAND)
       gs.Add(self.button5,0,wx.EXPAND)
       gs.Add(self.button6,0,wx.EXPAND)
       gs.Add(self.button7,0,wx.EXPAND)
       gs.Add(self.button8,0,wx.EXPAND)
       gs.Add(self.button9,0,wx.EXPAND)
       gs.Add(self.button10,0,wx.EXPAND)
       gs.Add(self.button11,0,wx.EXPAND)
       gs.Add(self.button12,0,wx.EXPAND)
       gs.Add(self.button13,0,wx.EXPAND)
       gs.Add(self.button14,0,wx.EXPAND)
       gs.Add(self.button15,0,wx.EXPAND)
       gs.Add(self.button16,0,wx.EXPAND)
       gs.Add(self.button17,0,wx.EXPAND)
       gs.Add(self.button18,0,wx.EXPAND)
       gs.Add(self.button19,0,wx.EXPAND)
       ms.Add(gs,1,wx.HORIZONTAL|wx.EXPAND|wx.ALL,5)
     
       self.SetSizer(ms)
    def on_button1(self,event):
        with open("calc.txt","r+") as file_handler:
            file_handler.truncate(0)
            file_handler.seek(0)
            wx.StaticText(self.display,label = "                        ")
            
    
    def on_button2(self,event):
        with open("calc.txt","r+")as file_handler:
            file =  file_handler.read()
            file_handler.close()
        with open("calc.txt","r+") as file_handler:
            i = len(file)
            file_handler.truncate(0)
            file_handler.seek(0)
            for i in range(i-1):
                file_handler.write(file[i])
            file = file_handler.read()
            
            self.display.SetLabelText(label = file)
            file_handler.close()
           
    def on_button3(self,event):
         self.Close()
         
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

