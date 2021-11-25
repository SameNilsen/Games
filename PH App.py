from tkinter import *
import tkinter as tk
#import tkMessageBox
import math as ma  
#from pylab import *
#import pandas as pd

top = Tk()

lst1 = ['Option1','Option2','Option3']
var1 = StringVar()
drop = OptionMenu(top,var1,*lst1)
drop.grid()

def a1():
    ka = var1.get()
    no = lst1.index(ka)
    Ka = float(data['Ka'][no])
    print(no)
    print(ka)
    print(Ka)

B=Button(top, text ="ok",command = a1).grid(row=1,column=1,)

top.mainloop()


