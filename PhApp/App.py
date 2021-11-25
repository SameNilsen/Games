from tkinter import *
from tkinter import messagebox
import tkinter as tk
import math as ma  
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
        L10 = Label(top, text="Masse",).grid(row=5,column=0)
        E10 = Entry(top, bd =5)
        E10.grid(row=5,column=1)
        Entry.insert(E10,0,0)
        L7 = Label(top, text="MolarMasse",).grid(row=6,column=0)
        E7 = Entry(top, bd =5)
        E7.grid(row=6,column=1)
        Entry.insert(E7,0,0)
        if x == 2:
            E8 = Entry(top, bd =5)
            E8.grid(row=0,column=1)
            Entry.insert(E8,0,'Sterk Syre')
        else:
            MM = float(data['Mm'][no])
            Entry.insert(E7,0,MM)
        def proces():
            global kons
            global E6
            L6 = Label(top, text="Ph",).grid(row=7,column=0)
            E6 = Entry(top, bd =5)
            E6.grid(row=7,column=1)
            if float(Entry.get(E4)) > 0:
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
            elif float(Entry.get(E3)) > 0:
                kons = float(Entry.get(E3))
                if x == 2:
                    Ph = -ma.log10(kons)
                    Entry.insert(E6,0,Ph)
                elif x == 14:
                    b3(2)
                elif x == 13:
                    b3(3) 
            elif float(Entry.get(E10)) > 0:
                m=float(Entry.get(E10))
                Mm=float(Entry.get(E7))
                v=float(Entry.get(E5))
                n = m/Mm
                kons = n/v
                if x == 2:
                    Ph = -ma.log10(kons)
                    Entry.insert(E6,0,Ph)
                elif x == 14:
                    b3(2)
                elif x == 13:
                    b3(3)
        B=Button(top, text ="Beregn",command = proces).grid(row=8,column=1,)
        
    def a2():
        E8 = Entry(top, bd =5)
        E8.grid(row=0,column=1)
        Entry.insert(E8,0,'Sterk Base')
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
        L10 = Label(top, text="Masse",).grid(row=5,column=0)
        E10 = Entry(top, bd =5)
        E10.grid(row=5,column=1)
        Entry.insert(E10,0,0)
        L7 = Label(top, text="MolarMasse",).grid(row=6,column=0)
        E7 = Entry(top, bd =5)
        E7.grid(row=6,column=1)
        Entry.insert(E7,0,0)
        def proces():
            global kons
            global E9
            L9 = Label(top, text="Ph",).grid(row=7,column=0)
            E9 = Entry(top, bd =5)
            E9.grid(row=7,column=1)
            if float(Entry.get(E4)) > 0:
                n=float(Entry.get(E4))
                v=float(Entry.get(E5))
                kons = n/v
                Ph = 14-(-ma.log10(kons))
                Entry.insert(E9,0,Ph)
            elif float(Entry.get(E3)) > 0:
                kons = float(Entry.get(E3))
                Ph = 14-(-ma.log10(kons))
                Entry.insert(E9,0,Ph)
            elif float(Entry.get(E10)) > 0:
                m=float(Entry.get(E10))
                Mm=float(Entry.get(E7))
                v=float(Entry.get(E5))
                n = m/Mm
                kons = n/v
                Ph = 14-(-ma.log10(kons))
                Entry.insert(E9,0,Ph)
        B=Button(top, text ="Beregn",command = proces).grid(row=8,column=1,)
        
    def a3(y):
        lst1 = ['HO2C2O2H','H2SO3','HSO4-','H3PO4','HNO2','HF','HCO2H','C6H5COOH','HO2C2O2-','CH3COOH','CO3 2-','H2S','H2PO4-','HS-','HCIO','HCN','NH4+','H3BO3','HCO3-','HPO4 2-','H2BO3-','HS-','HBO3 2-']
        var1 = StringVar()
        drop = OptionMenu(top,var1,*lst1)
        if y == 1:
            E8 = Entry(top, bd =5)
            E8.grid(row=0,column=1)
            Entry.insert(E8,0,'Svak Syre')
        elif y == 2:
            E8 = Entry(top, bd =5)
            E8.grid(row=0,column=1)
            Entry.insert(E8,0,'Svak Base')
        def b4():
            global no
            global ka
            stoff = var1.get()
            no = lst1.index(stoff)
            print(no)
            print(stoff)
            if y == 1:
                ka = float(data['Ka'][no])
                p = 14
            elif y == 2:
                ka = (10**(-14))/float(data['Ka'][no])
                p = 13
            Button(top, text ="Ok",command = lambda:a1(p)).grid(row=11,column=3,)
        if y == 1:
            L = Label(top, text="Velg syre",).grid(row=2,column=2)
            drop.grid(row=3, column=2)
            Button(top, text ="Velg",command = b4).grid(row=4,column=2,)
        elif y == 2:
            L1 = Label(top, text="Velg korresponderende syre",).grid(row=2,column=3)
            drop.grid(row=3, column=3)
            Button(top, text ="Velg",command = b4).grid(row=4,column=3,)
        def b2():
            global ka
            if y == 1:
                L3 = Label(top, text="Ka:",).grid(row=10,column=2)
                E3 = Entry(top, bd =5)
                E3.grid(row=10,column=3)
                ka = Entry.get(E3)
                p = 14
            elif y == 2:
                L3 = Label(top, text="Ka til korresponderende syre:",).grid(row=10,column=0)
                E3 = Entry(top, bd =5)
                E3.grid(row=10,column=1)
                kb = float(Entry.get(E3))
                ka = (10**(-14))/kb
                p = 13
            Button(top, text ="Ok",command = lambda:a1(p)).grid(row=11,column=3,)
        L2 = Label(top, text="Er ikke stoffet på lista?",).grid(row=9,column=2)
        Button(top, text ="Nei :(",command = b2).grid(row=9,column=3,)
    
    E8 = Entry(top, bd =5)
    E8.grid(row=0,column=1)
    Entry.insert(E8,0,'Velg Stofftype')
    top.title("Ph kalkulator")
    A=Button(top, text ="Sterk Syre",command = lambda:a1(2)).grid(row=1,column=0,)
    C=Button(top, text ="Sterk Base",command = a2).grid(row=1,column=1,)
    D=Button(top, text ="Svak Syre",command = lambda:a3(1)).grid(row=1,column=2,)
    E=Button(top, text ="Svak Base",command = lambda:a3(2)).grid(row=1,column=3,)

F=Button(top, text ="Start",command = f).grid(row=0,column=0,)


top.mainloop()