from tkinter import *
from tkinter import messagebox
import tkinter as tk
#import Tkinter
#import tkMessageBox
import math as ma  
#from pylab import *
import pandas as pd 
data = pd.read_csv('Stoffer.csv', sep = ";", encoding = "ISO-8859-1")

top = Tk()

def f():
    def b3(g):
        global kons
        c = float(ka*kons*-1)
        if g == 2:
            x_1 = (-1*(ka) + ma.sqrt((ka)**2 -4*c))/2
            Ph = -ma.log10(x_1)
            print(Ph)
            Entry.insert(E6,0,Ph)
        elif g == 3:
            x_1 = (-1*(ka) + ma.sqrt((ka)**2 -4*c))/2
            Ph = 14-(-ma.log10(x_1))
            print(Ph)
            Entry.insert(E6,0,Ph)
    
    def a1(x):
        L3 = Label(top, text="Konsentrasjon",).grid(row=x,column=0)
        E3 = Entry(top, bd =5)
        E3.grid(row=x,column=1)
        Entry.insert(E3,0,0)
        L4 = Label(top, text="Stoffmengde",).grid(row=1+x,column=0)
        E4 = Entry(top, bd =5)
        E4.grid(row=1+x,column=1)
        Entry.insert(E4,0,0)
        L5 = Label(top, text="Volum",).grid(row=2+x,column=0)
        E5 = Entry(top, bd =5)
        E5.grid(row=2+x,column=1)
        Entry.insert(E5,0,0)
        def proces():
            global kons
            global E6
            L6 = Label(top, text="Ph",).grid(row=3+x,column=0)
            E6 = Entry(top, bd =5)
            E6.grid(row=3+x,column=1)
            if float(Entry.get(E3)) == 0:
                n=float(Entry.get(E4))
                v=float(Entry.get(E5))
                kons = n/v
                if x == 2:
                    Ph = -ma.log10(kons)
                    Entry.insert(E6,0,Ph)
                elif x == 14:
                    b3(2)
                elif x == 13:
                    b3(3)
            else:
                kons = float(Entry.get(E3))
                if x == 2:
                    Ph = -ma.log10(kons)
                    Entry.insert(E6,0,Ph)
                elif x == 14:
                    b3(2)
                elif x == 13:
                    b3(3)    
        B=Button(top, text ="Beregn",command = proces).grid(row=4+x,column=1,)
        
    def a2():
        L3 = Label(top, text="Konsentrasjon",).grid(row=2,column=0)
        E3 = Entry(top, bd =5)
        E3.grid(row=2,column=1)
        Entry.insert(E3,0,0)
        L4 = Label(top, text="Stoffmengde",).grid(row=3,column=0)
        E4 = Entry(top, bd =5)
        E4.grid(row=3,column=1)
        Entry.insert(E4,0,0)
        L5 = Label(top, text="Volum",).grid(row=4,column=0)
        E5 = Entry(top, bd =5)
        E5.grid(row=4,column=1)
        Entry.insert(E5,0,0)
        def proces():
            global kons
            L6 = Label(top, text="Ph",).grid(row=5,column=0)
            E6 = Entry(top, bd =5)
            E6.grid(row=5,column=1)
            if float(Entry.get(E3)) == 0:
                n=float(Entry.get(E4))
                v=float(Entry.get(E5))
                global kons
                kons = n/v
                Ph = 14-(-ma.log10(kons))
                Entry.insert(E6,0,Ph)
            else:
                kons = float(Entry.get(E3))
                Ph = 14-(-ma.log10(kons))
                Entry.insert(E6,0,Ph)
        B=Button(top, text ="Beregn",command = proces).grid(row=6,column=1,)
        
    def a3(y):
        lst1 = ['Option1','Option2','Option3']
        var1 = StringVar()
        drop = OptionMenu(top,var1,*lst1)
        drop.grid(row=3, column=4)
        if y == 1:
            L = Label(top, text="Velg syre",).grid(row=2,column=1)
        elif y == 2:
            L1 = Label(top, text="Velg korresponderende syre",).grid(row=2,column=1)
        Button(top, text ="HO2C2O2H",command = lambda: b1(0)).grid(row=3,column=0,)
        Button(top, text ="H2SO3",command = lambda: b1(1)).grid(row=3,column=1,)
        Button(top, text ="HCIO",command = lambda: b1(14)).grid(row=3,column=2,)
        Button(top, text ="HSO4-",command = lambda: b1(2)).grid(row=3,column=3,)
        Button(top, text ="H3PO4",command = lambda: b1(3)).grid(row=4,column=0,)
        Button(top, text ="HNO2",command = lambda: b1(4)).grid(row=4,column=1,)
        Button(top, text ="HF",command = lambda: b1(5)).grid(row=4,column=2,)
        Button(top, text ="HCO2H",command = lambda: b1(6)).grid(row=4,column=3,)
        Button(top, text ="C6H5COOH",command = lambda: b1(7)).grid(row=5,column=0,)
        Button(top, text ="HO2C2O2-",command = lambda: b1(8)).grid(row=5,column=1,)
        Button(top, text ="CH3COOH",command = lambda: b1(9)).grid(row=5,column=2,)
        Button(top, text ="CO3 2-",command = lambda: b1(10)).grid(row=5,column=3,)
        Button(top, text ="H2S",command = lambda: b1(11)).grid(row=6,column=0,)
        Button(top, text ="H2PO4-",command = lambda: b1(12)).grid(row=6,column=1,)
        Button(top, text ="HS-",command = lambda: b1(13)).grid(row=6,column=2,)
        Button(top, text ="HCN",command = lambda: b1(15)).grid(row=6,column=3,)
        Button(top, text ="NH4+",command = lambda: b1(16)).grid(row=7,column=0,)
        Button(top, text ="H3BO3",command = lambda: b1(17)).grid(row=7,column=1,)
        Button(top, text ="HCO3-",command = lambda: b1(18)).grid(row=7,column=2,)
        Button(top, text ="HPO4 2-",command = lambda: b1(19)).grid(row=7,column=3,)
        Button(top, text ="H2BO3-",command = lambda: b1(20)).grid(row=8,column=0,)
        Button(top, text ="HS-",command = lambda: b1(21)).grid(row=8,column=1,)
        Button(top, text ="HBO3 2-",command = lambda: b1(22)).grid(row=8,column=2,)
        def b4():
            stoff = var1.get()
            no = lst1.index(stoff)
            print(no)
            print(ka)
            print(Ka)
            if y == 1:
                Ka = float(data['Ka'][no])
            elif y == 2:
                Ka = (10**(-14))/float(data['Ka'][no])
            Button(top, text ="Ok",command = lambda:a1(p)).grid(row=11,column=1,)
        Button(top, text ="Okk",command = b4).grid(row=4,column=4,)
        def b1(x):
            global ka
            #E2 = Entry(top, bd =5)
            #E2.grid(row=9,column=1)
            if y == 2:
                ka = (10**(-14))/data['Ka'][x]
                #Entry.insert(E2,0,u)
                p = 13
            elif y == 1:
                ka = float(data['Ka'][x])
                #Entry.insert(E2,0,u)
                p = 14
            Button(top, text ="Ok",command = lambda:a1(p)).grid(row=11,column=1,)
        def b2():
            global ka
            if y == 1:
                L3 = Label(top, text="Ka:",).grid(row=10,column=0)
                E3 = Entry(top, bd =5)
                E3.grid(row=10,column=1)
                ka = Entry.get(E3)
                p = 14
            elif y == 2:
                L3 = Label(top, text="Ka til korresponderende syre:",).grid(row=10,column=0)
                E3 = Entry(top, bd =5)
                E3.grid(row=10,column=1)
                kb = float(Entry.get(E3))
                ka = (10**(-14))/kb
                p = 13
            Button(top, text ="Ok",command = lambda:a1(p)).grid(row=11,column=1,)
        L2 = Label(top, text="Er ikke stoffet på lista?",).grid(row=9,column=0)
        Button(top, text ="Nei :(",command = b2).grid(row=9,column=1,)
    
    L1 = Label(top, text="Ph kalkulator",).grid(row=0,column=1)
    top.title("Ph kalkulator")
    A=Button(top, text ="Sterk Syre",command = lambda:a1(2)).grid(row=1,column=0,)
    C=Button(top, text ="Sterk Base",command = a2).grid(row=1,column=1,)
    D=Button(top, text ="Svak Syre",command = lambda:a3(1)).grid(row=1,column=2,)
    E=Button(top, text ="Svak Base",command = lambda:a3(2)).grid(row=1,column=3,)

F=Button(top, text ="Start/Reset",command = f).grid(row=1,column=4,)

"""
var = StringVar(top)
var.set("one") # initial value

option = OptionMenu(top, var, "one", "two", "three", "four")
#option.pack()

#
# test stuff

def ok():
    print("value is", var.get())
    top.quit()

button = Button(top, text="OK", command=ok)
#button.pack()
"""

"""
L3 = Label(top, text="Konsentrasjon",).grid(row=2,column=0)
L4 = Label(top, text="Stoffmengde",).grid(row=3,column=0)
L4 = Label(top, text="Ph",).grid(row=4,column=0)
E2 = Entry(top, bd =5)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =5)
E3.grid(row=3,column=1)
E4 = Entry(top, bd =5)
E4.grid(row=4,column=1)
"""

top.mainloop()