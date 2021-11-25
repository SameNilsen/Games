# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 20:09:46 2019

@author: MortenNilsen
"""
import pylab as pl
from math import *

import pandas as pd
"""
data = pd.read_csv('Stoffer.csv', sep = ";", encoding = "ISO-8859-1") 
print(data)
print(data['Mm'][3])
liste = []
#liste.append(data['Stoff'])
#p = input("Hvilken korresoirdende syre?")
Ka = 10/1

print(liste[1])
for i in range(11):
    liste.append
"""
data1 = pd.read_csv('MolarMasse.csv', sep = ";", encoding = "ISO-8859-1")
liste2 = []
Mm = 0
for i in range(24):
    Mm = 0
    y = 1
    for i in range(100):
        a = input("Grunnstoff",y,":")
        if a == "c":
            g = float(input("Hvor mange:"))
            Mm += g*12
            y += 1
        elif a == "h":
            g = float(input("Hvor mange:"))
            Mm += g*1
        elif a == "he":
            g = float(input("Hvor mange:"))
            Mm += g*4
        elif a == "na":
            g = float(input("Hvor mange:"))
            Mm += g*23
        elif a == "n":
            g = float(input("Hvor mange:"))
            Mm += g*14
        elif a == "o":
            g = float(input("Hvor mange:"))
            Mm += g*16
        elif a == "cl":
            g = float(input("Hvor mange:"))
            Mm += g*35.45
        elif a == "b":
            g = float(input("Hvor mange:"))
            Mm += g*10.8
        elif a == "p":
            g = float(input("Hvor mange:"))
            Mm += g*31
        elif a == "s":
            g = float(input("Hvor mange:"))
            Mm += g*32
        elif a == "f":
            g = float(input("Hvor mange:"))
            Mm += g*19
        elif a == "e":
            break
    print(Mm)
    liste2.append(Mm)
    print(liste2)
    qq = input("End?")
    if qq == "ja":
        break
print(liste2)
[60.0, 34.0, 97.0, 33.0, 52.45, 27.0, 18.0, 61.8, 61.0, 96.0, 60.8, 33.0, 59.8]