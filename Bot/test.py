from tkinter import *
master = Tk()

def run_all():
    var1.set(1)
    var2.set(1)
    var3.set(1)
    var4.set(1)
    ad()
    sub()
    mul()
    div()
    master.destroy()

def ad():
    if(var1.get()==1):
        print(5+5)
def sub():
    if(var2.get()==1):
        print(5-5)
def mul():
    if(var3.get()==1):
        print(5*5)
def div():
    if(var4.get()==1):
        print(5/5)
Label(master, text="Operations:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="Add", variable=var1,command=ad).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="Subtract", variable=var2,command=sub).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="Multiply", variable=var3,command=mul).grid(row=3, sticky=W)
var4 = IntVar()
Checkbutton(master, text="Divide", variable=var4,command=div).grid(row=4, sticky=W)
Button(master, text='Run', command=run_all).grid(row=5, sticky=W, pady=4)
mainloop()