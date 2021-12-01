from numpy import minimum
from pyautogui import *
import pyautogui
import pyautogui as pt
from tkinter import *
import tkinter as tk
import threading 
from tkinter import messagebox 
import win32gui, win32con

#the_program_to_hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)


nigga = 0 
#karczma 
class Clicker:
    def __init__(self, target_png, speed):
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=.8)  # region=(0, 84, 1277, 793)
            pt.moveTo(position[0] + 15, position[1] + 15, duration=self.speed)
            pt.doubleClick()
            return 0

        except:
            textbox.delete(1.0, END)
            textbox.insert(tk.END,  "Program został uruchomiony: ")
            return 1
            
    def check_sprawdzanie_czy_ma_fiuta():
        xd = r'C:\Users\Niger\Desktop\Bot\imagine\reklamy\zabezpieczenia\1.png'
        if pt.locateOnScreen(xd, confidence=.8):
            return 1
        else:
            return 2



def karczma():
    
    start = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\Start\1.png', speed=.1)


    hero1 = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\hero\1.png', speed=.1)
    hero2 = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\hero\2.png', speed=.1)
    hero3 = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\hero\3.png', speed=.1)
    hero4 = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\hero\4.png', speed=.1)
    hero5 = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\hero\5.png', speed=.1)
    hero6 = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\hero\6.png', speed=.1)
    hero7 = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\hero\7.png', speed=.1)
    hero8 = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\hero\8.png', speed=.1)

    confirm = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\confirm\1.png', speed=.1)
    confirm2 = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\confirm\2.png', speed=.1)
   
    
    while True:
        start.nav_to_image()
        hero1.nav_to_image()
        hero2.nav_to_image()
        hero3.nav_to_image()
        hero4.nav_to_image()
        hero5.nav_to_image()
        hero6.nav_to_image()
        hero7.nav_to_image()
        hero8.nav_to_image()
        confirm.nav_to_image()
        confirm2.nav_to_image()

def lochy():
    startlochy = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\Start\2.png', speed=.1)
    lochy = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\lochy\1.png', speed=.1)
    bitwalochy = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\Start\3.png', speed=.1)

    while 1:
        startlochy.nav_to_image()
        lochy.nav_to_image()
        if bitwalochy.nav_to_image() == 0:
            time.sleep(3600)

def Reklamy():
    startreklamy = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\Start\1.png', speed=.1)
    reklama = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\reklamy\1.png', speed=.1)
    #skip = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\reklamy\2.png', speed=.1)
    #skip1 = Clicker(r'C:\Users\Niger\Desktop\Bot\imagine\reklamy\3.png', speed=.1)

    while 1:
        startreklamy.nav_to_image()
        if reklama.nav_to_image() == 0:
            time.sleep(32)
            pyautogui.press('esc')

def stop():
    quit()
##############################################################GUI
root = Tk()
root.title("Bot Szmata do jebania wersia demo alpaha 1.0 ")
root.geometry('570x300')
textbox = tk.Text(root, width = 70, height = 16)
textbox.pack()
textbox.place(x=2, y=30)
#HWDP
def StopLag():
    threading.Thread(target=karczma).start()

def StopLag1():
    threading.Thread(target=lochy).start()

def StopLag2():
    threading.Thread(target=Reklamy).start()

def chceckut():
    if var.get() == 5 and var1.get() == 5 and var2.get() == 5:
        but1['state'] = DISABLED 
    elif var.get() == 5 and var1.get() == 5:   
        but1['state'] = DISABLED
    elif var2.get() == 5 and var1.get() == 5:   
        but1['state'] = DISABLED   
    elif var.get() == 5:
        but1['state'] = NORMAL
        but1.configure(command = StopLag)   
    elif var1.get() == 5:
        but1['state'] = NORMAL
        but1.configure(command= StopLag1)            
    elif var2.get() == 5:
        but1['state'] = NORMAL
        but1.configure(command= StopLag2)            
    elif var.get() == 10:
        but1['state'] = DISABLED        
    else:
        messagebox.showerror('Czarny błąd', 'Coś poszło nie tak czarnuchu!')   


var = IntVar(value=10)
Checkbutton(root, text='Karczma: ',variable=var, onvalue=5, offvalue=10, command=chceckut).grid(row=0, column=0, sticky=W)

var1 = IntVar(value=10)
Checkbutton(root, text='Lochy: ', variable=var1,  onvalue=5, offvalue=10, command=chceckut).grid(row=0, column=1, sticky=W)

var2 = IntVar(value=10)
Checkbutton(root, text='Reklamy: ', variable=var2,  onvalue=5, offvalue=10, command=chceckut).grid(row=0, column=2, sticky=W)

but1 = Button(root, text="Start", state=DISABLED)
but1.place(x = 265, y= 0)

but2 = Button(root, text="Exit", command=stop)
but2.place(x = 300, y= 0)



root.mainloop()