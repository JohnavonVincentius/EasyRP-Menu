import tkinter as tk
import tkinter.font as tkFont
import configparser
import time
import math
import subprocess
from subprocess import Popen
import os

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

def UpdtTime():
    currtime = math.floor(time.time())
    config.set('State','StartTimestamp', str(currtime))
    UpdtFile()


def SetStatus(State,Details,LT,ST):
    config.set('State','State', State)
    config.set('State','Details', Details)
    config.set('Images','LargeImageTooltip', LT)
    config.set('Images','SmallImageTooltip', ST)

def SetImg(Big,Small):
    config.set('Images','SmallImage', Small)
    config.set('Images','LargeImage', Big)

def UpdtFile():
    file = open('config.ini', 'w+') 
    config.write(file,space_around_delimiters=False)
    file.close()


def ZoomInit():
    ZoomUpdt()
    UpdtTime()

def ZoomUpdt():
    Size = GLineEdit_887.get()
    Max = GLineEdit_734.get()
    SetStatus("Zooming (" + str(Size) + "/" + str(Max) + ")","With My Classmates","Zooming","Online")
    SetImg("zoom","zooms")
    UpdtFile()

def GButton_383_command():
    GButton_701_command()
    UpdtTime()


def GButton_879_command():
    GButton_476_command()
    UpdtTime()

def GButton_701_command():
    Size = GLineEdit_711.get()
    Max = GLineEdit_605.get()
    World = GLineEdit_357.get()
    SetStatus(World,"Playing Minecraft (" + str(Size) + "/" + str(Max) + ")","Playing Minecraft",World)
    SetImg("minecraft","diamond")
    UpdtFile()


def GButton_476_command():
    Status = GLineEdit_44.get()
    Details = GLineEdit_895.get()
    SIText = GLineEdit_781.get()
    LIText = GLineEdit_172.get()
    LImg = GLineEdit_908.get()
    SImg = GLineEdit_108.get()
    SetStatus(Status,Details,LIText,SIText)
    SetImg(LImg,SImg)
    UpdtFile()


if process_exists("easyrp.exe") == False:
    subprocess.Popen("easyrp.exe")

config = configparser.ConfigParser()
config.optionxform = str
config.space_around_delimiters = False
config.read('config.ini')

root = tk.Tk()
#setting title
root.title("Discord Custom Status Menu")
#setting window size
width=300
height=450
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

GButton_800=tk.Button(root)
GButton_800["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_800["font"] = ft
GButton_800["fg"] = "#000000"
GButton_800["justify"] = "center"
GButton_800["text"] = "Zoom"
GButton_800.place(x=0,y=40,width=100,height=25)
GButton_800["command"] = ZoomInit

GLabel_240=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_240["font"] = ft
GLabel_240["fg"] = "#333333"
GLabel_240["justify"] = "center"
GLabel_240["text"] = "Discord Custom Status"
GLabel_240.place(x=0,y=0,width=300,height=25)

GButton_383=tk.Button(root)
GButton_383["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_383["font"] = ft
GButton_383["fg"] = "#000000"
GButton_383["justify"] = "center"
GButton_383["text"] = "Minecraft"
GButton_383.place(x=140,y=40,width=100,height=25)
GButton_383["command"] = GButton_383_command

GButton_879=tk.Button(root)
GButton_879["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_879["font"] = ft
GButton_879["fg"] = "#000000"
GButton_879["justify"] = "center"
GButton_879["text"] = "Custom Status"
GButton_879.place(x=90,y=200,width=100,height=25)
GButton_879["command"] = GButton_879_command

GButton_711=tk.Button(root)
GButton_711["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_711["font"] = ft
GButton_711["fg"] = "#000000"
GButton_711["justify"] = "center"
GButton_711["text"] = "Restart Time"
GButton_711.place(x=190,y=410,width=100,height=25)
GButton_711["command"] = UpdtTime

GLineEdit_887=tk.Entry(root)
GLineEdit_887["borderwidth"] = "1px"
GLineEdit_887["cursor"] = "arrow"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_887["font"] = ft
GLineEdit_887["fg"] = "#333333"
GLineEdit_887["justify"] = "center"
GLineEdit_887["text"] = ""
GLineEdit_887["relief"] = "flat"
GLineEdit_887.place(x=50,y=70,width=50,height=25)

GLineEdit_711=tk.Entry(root)
GLineEdit_711["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_711["font"] = ft
GLineEdit_711["fg"] = "#333333"
GLineEdit_711["justify"] = "center"
GLineEdit_711["text"] = ""
GLineEdit_711["relief"] = "flat"
GLineEdit_711.place(x=190,y=70,width=50,height=25)

GLineEdit_895=tk.Entry(root)
GLineEdit_895["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_895["font"] = ft
GLineEdit_895["fg"] = "#333333"
GLineEdit_895["justify"] = "center"
GLineEdit_895["text"] = "NONE"
GLineEdit_895["relief"] = "flat"
GLineEdit_895.place(x=60,y=230,width=230,height=25)

GLabel_894=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_894["font"] = ft
GLabel_894["fg"] = "#333333"
GLabel_894["justify"] = "center"
GLabel_894["text"] = "Size :"
GLabel_894.place(x=0,y=70,width=50,height=25)

GLabel_781=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_781["font"] = ft
GLabel_781["fg"] = "#333333"
GLabel_781["justify"] = "center"
GLabel_781["text"] = "Max : "
GLabel_781.place(x=0,y=100,width=50,height=25)

GLineEdit_734=tk.Entry(root)
GLineEdit_734["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_734["font"] = ft
GLineEdit_734["fg"] = "#333333"
GLineEdit_734["justify"] = "center"
GLineEdit_734["text"] = ""
GLineEdit_734.place(x=50,y=100,width=50,height=25)

GLabel_790=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_790["font"] = ft
GLabel_790["fg"] = "#333333"
GLabel_790["justify"] = "center"
GLabel_790["text"] = "Size : "
GLabel_790.place(x=140,y=70,width=50,height=25)

GLabel_525=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_525["font"] = ft
GLabel_525["fg"] = "#333333"
GLabel_525["justify"] = "center"
GLabel_525["text"] = "Max :"
GLabel_525.place(x=140,y=100,width=50,height=25)

GLineEdit_605=tk.Entry(root)
GLineEdit_605["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_605["font"] = ft
GLineEdit_605["fg"] = "#333333"
GLineEdit_605["justify"] = "center"
GLineEdit_605["text"] = ""
GLineEdit_605.place(x=190,y=100,width=50,height=25)

GLineEdit_357=tk.Entry(root)
GLineEdit_357["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_357["font"] = ft
GLineEdit_357["fg"] = "#333333"
GLineEdit_357["justify"] = "center"
GLineEdit_357["text"] = ""
GLineEdit_357.place(x=190,y=130,width=100,height=25)

GButton_821=tk.Button(root)
GButton_821["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_821["font"] = ft
GButton_821["fg"] = "#000000"
GButton_821["justify"] = "center"
GButton_821["text"] = "Update"
GButton_821.place(x=0,y=130,width=100,height=25)
GButton_821["command"] = ZoomUpdt

GButton_701=tk.Button(root)
GButton_701["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_701["font"] = ft
GButton_701["fg"] = "#000000"
GButton_701["justify"] = "center"
GButton_701["text"] = "Update"
GButton_701.place(x=140,y=160,width=100,height=25)
GButton_701["command"] = GButton_701_command

GLabel_533=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_533["font"] = ft
GLabel_533["fg"] = "#333333"
GLabel_533["justify"] = "center"
GLabel_533["text"] = "Status :"
GLabel_533.place(x=0,y=230,width=70,height=25)

GLabel_252=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_252["font"] = ft
GLabel_252["fg"] = "#333333"
GLabel_252["justify"] = "center"
GLabel_252["text"] = "Details :"
GLabel_252.place(x=0,y=260,width=70,height=25)

GLabel_932=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_932["font"] = ft
GLabel_932["fg"] = "#333333"
GLabel_932["justify"] = "center"
GLabel_932["text"] = "SI Text :"
GLabel_932.place(x=0,y=290,width=70,height=25)

GLabel_956=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_956["font"] = ft
GLabel_956["fg"] = "#333333"
GLabel_956["justify"] = "center"
GLabel_956["text"] = "World:"
GLabel_956.place(x=140,y=130,width=50,height=25)

GLabel_476=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_476["font"] = ft
GLabel_476["fg"] = "#333333"
GLabel_476["justify"] = "center"
GLabel_476["text"] = "LI Text :"
GLabel_476.place(x=0,y=320,width=70,height=25)

GLabel_276=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_276["font"] = ft
GLabel_276["fg"] = "#333333"
GLabel_276["justify"] = "center"
GLabel_276["text"] = "L Img :"
GLabel_276.place(x=0,y=350,width=70,height=25)

GLabel_148=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_148["font"] = ft
GLabel_148["fg"] = "#333333"
GLabel_148["justify"] = "center"
GLabel_148["text"] = "S Img :"
GLabel_148.place(x=0,y=380,width=70,height=25)

GLineEdit_44=tk.Entry(root)
GLineEdit_44["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_44["font"] = ft
GLineEdit_44["fg"] = "#333333"
GLineEdit_44["justify"] = "center"
GLineEdit_44["text"] = ""
GLineEdit_44.place(x=60,y=260,width=230,height=25)

GLineEdit_781=tk.Entry(root)
GLineEdit_781["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_781["font"] = ft
GLineEdit_781["fg"] = "#333333"
GLineEdit_781["justify"] = "center"
GLineEdit_781["text"] = ""
GLineEdit_781.place(x=60,y=290,width=230,height=25)

GLineEdit_172=tk.Entry(root)
GLineEdit_172["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_172["font"] = ft
GLineEdit_172["fg"] = "#333333"
GLineEdit_172["justify"] = "center"
GLineEdit_172["text"] = ""
GLineEdit_172.place(x=60,y=320,width=230,height=25)

GLineEdit_908=tk.Entry(root)
GLineEdit_908["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_908["font"] = ft
GLineEdit_908["fg"] = "#333333"
GLineEdit_908["justify"] = "center"
GLineEdit_908["text"] = ""
GLineEdit_908.place(x=60,y=350,width=230,height=25)

GLineEdit_108=tk.Entry(root)
GLineEdit_108["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_108["font"] = ft
GLineEdit_108["fg"] = "#333333"
GLineEdit_108["justify"] = "center"
GLineEdit_108["text"] = ""
GLineEdit_108.place(x=60,y=380,width=230,height=25)

GButton_476=tk.Button(root)
GButton_476["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_476["font"] = ft
GButton_476["fg"] = "#000000"
GButton_476["justify"] = "center"
GButton_476["text"] = "Update"
GButton_476.place(x=10,y=410,width=100,height=25)
GButton_476["command"] = GButton_476_command

root.mainloop()

