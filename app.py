from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import threading
import time 
import os
import shutil
import pytz          
import subprocess
import datetime
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Dialog Widget")
        self.minsize(400, 400)
        self.interface()
        self.ngrok()

    def interface(self):
        self.labelFrame = ttk.LabelFrame(self, text = "Locate the server.jar file")
        self.labelFrame.grid( row = 0, column = 0, padx = 10, pady = 10)

        self.name_var = StringVar()
        self.name_entry = ttk.Entry(self.labelFrame,textvariable ="", font=('calibre',10,'normal'),width=40)
        self.name_entry.grid(row=1,column=0)
        
        self.button = ttk.Button(self.labelFrame, text = "browse",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)
        

        self.labelFrame2 = ttk.LabelFrame(self, text = "Settings")
        self.labelFrame2.grid( row = 2, column = 0)

        self.labelgamemode = ttk.Label(self.labelFrame2,text="GAMEMODE : ")
        self.labelgamemode.grid(row=0,column=0)

        self.gamemode_string = StringVar()
        self.monthchoosen = ttk.Combobox(self.labelFrame2, width = 27, textvariable = self.gamemode_string)
        self.monthchoosen['values'] = (' SURVIVAL',  
                          ' CREATIVE', 
                          ' SPECTATOR', 
                          ' ADVENTURE', 
                          ) 
        self.monthchoosen.grid(row = 0, column = 1) 
        self.monthchoosen.current()

        self.monthchoosen = ttk.Combobox(self.labelFrame2, width = 27, textvariable = self.gamemode_string)
        self.monthchoosen['values'] = (' SURVIVAL',  
                          ' CREATIVE', 
                          ' SPECTATOR', 
                          ' ADVENTURE', 
                          ) 
        self.monthchoosen.grid(row = 0, column = 1) 
        self.monthchoosen.current()

        self.hardcore = IntVar()
        self.harcoreCheck = ttk.Checkbutton(self.labelFrame2,text = "HARDCORE", variable=self.hardcore, onvalue = 1, offvalue = 0,width = 20,command=self.setHardcore)
        self.harcoreCheck.grid(row=1,column=1)

        self.cracked = IntVar()
        self.crackedCheck = ttk.Checkbutton(self.labelFrame2,text = "CRACKED", variable=self.cracked, onvalue = 1, offvalue = 0,width = 20,command=self.setcracked)
        self.crackedCheck.grid(row=2,column=1)

        

    def ngrok(self):
        self.ngrokFrame = ttk.LabelFrame(self, text = "Enter ngrok Alt token")
        self.ngrokFrame.grid( row = 3, column = 0, padx = 10, pady = 10)
        
        self.alt = StringVar()
        self.alt_entry = ttk.Entry(self.ngrokFrame,textvariable ="", font=('calibre',10,'normal'),width=40)
        self.alt_entry.grid(row=1,column=0)


        self.tclable = ttk.Label(self,text="\tYou are Accepting EULA Agreement \n(https://account.mojang.com/documents/minecraft_eula).")
        self.tclable.grid(row=4,column=0)
        
        self.tc = IntVar()
        self.tcCheck = ttk.Checkbutton(self,text = "EULA TC", variable=self.tc, onvalue = 1, offvalue = 0,width = 20,command=self.accepttc)
        self.tcCheck.grid(row=5,column=0)
        
        self.counter = 0
        self.btn_text = StringVar()
        self.btn_text.set("START")
        self.buttongo = ttk.Button(self, textvariable=self.btn_text,command = self.createfile,state="disable")
        self.buttongo.grid(row = 6, column = 0)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        self.name_var.set(self.filename)
        self.name_entry.insert(0,self.name_var.get())

    def setHardcore(self):
        if(self.hardcore.get()==1):
            self.monthchoosen.configure(state="disabled")

        else:
            self.monthchoosen.configure(state="enable")
        return

    def setcracked(self):
        return

    def serverpropcreater(self):
        return

    def setmonth(self):
        self.gamemode_string.set(self.monthchoosen)
        print(self.gmamode_sring)

    def createfile(self):
        self.counter +=1

        if(self.counter %2==0):
            self.btn_text.set("STOP")
        path= os.getcwd()
        try:
            create = path+"\\"+"Minecraft server"
            os.mkdir(create)
        except:
            print("Already Exists")
        # try:
        #     with open('.\Minecraft server\run.bat','w+') as f:
        #         f.write('start "mcraft" java -Xmx1024M -Xms1024M -jar server.jar nogui')
        # try:
        #     with open('.\Minecraft server\stop.bat','w+') as f:
        #         f.write('taskkill /FI "WindowTitle eq mcraft*" /T /F')    
        # except:
        #     print("error")
            
        shutil.copy(self.name_var.get(), create)

        return

    def accepttc(self):
        if(self.tc.get()==1):
            self.buttongo.configure(state="enable")
            self._accepttc = 'true'
            
        else:
            self.buttongo.configure(state="disable")
            self._accepttc = 'false'

        self.eulawrite(self._accepttc)
        return

    def eulawrite(self,value):
        with open('.\Minecraft server\eula.txt','w+') as f:
                f.write("#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n")
                datetimeVar = datetime.datetime.now()
                localtime = datetimeVar.strftime("%c")
                f.write("#"+localtime[:8]+datetimeVar.strftime("%d")+localtime[10:])
                f.write("\nelue = "+str(value))
        return

    def serverwrite(self):
        
        return

    
root = Root()

root.mainloop()