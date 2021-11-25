from tkinter import *
import tkinter as tk
#import tkMessageBox
import math as ma  
#from pylab import *
#import pandas as pd
from tkinter import ttk
def proces():
    a = Entry.get(E4)
    #b = float(Entry.get(E4))
    c = Entry.get(E2)
    #d = float(Entry.get(E2))
    if isinstance(a, float):
        n=float(Entry.get(E3))
        v=float(Entry.get(E4))
        kons = n/v
        Ph = 14-(-ma.log10(kons))
        Entry.insert(E5,0,Ph)
    elif isinstance(c, float):
        kons = float(Entry.get(E2))
        Ph = 14-(-ma.log10(kons))
        Entry.insert(E5,0,Ph)
    
def a1():
    kons=float(Entry.get(E2))
    Konsentrasjon = -ma.log10(kons)
    Entry.insert(E4,0,Konsentrasjon)
    print(Konsentrasjon)

def a2():
    print("HH")
    
def a3():
    print("KKK")
    
def a4():
    Button(top, text ="Svak Base",command = a4).grid(row=6,column=1,)
    
def a5():
    print("HEU")
lst1 = ['Option1','Option2','Option3']
var1 = StringVar()
drop = OptionMenu(top,var1,*lst1)
drop.grid(row=3, column=4)


x=1
top = Tk()
L1 = Label(top, text="Ph kalkulator",).grid(row=0,column=1)
A=Button(top, text ="Sterk Syre",command = a2 and a5).grid(row=1,column=0,)
C=Button(top, text ="Sterk Base",command = a2).grid(row=1,column=1,)
D=Button(top, text ="Svak Syre",command = a3).grid(row=1,column=2,)
E=Button(top, text ="Svak Base",command = a4).grid(row=1+x,column=3,)
L3 = Label(top, text="Konsentrasjon",).grid(row=2,column=0)
L4 = Label(top, text=x,).grid(row=3,column=0)
L4 = Label(top, text="Volum",).grid(row=4,column=0)
E2 = Entry(top, bd =5)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =5)
E3.grid(row=3,column=1)
E4 = Entry(top, bd =5)
E4.grid(row=4,column=1)
E5 = Entry(top, bd =5)
E5.grid(row=6,column=1)
L5 = Label(top, text="Ph",).grid(row=6,column=0)
B=Button(top, text ="Beregn",command = proces).grid(row=5,column=1,)
Entry.insert(E5,0,"-")

top.mainloop()