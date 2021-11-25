# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:04:27 2019

@author: MortenNilsen
"""
from pylab import *

u = int(input("Skriv inn tall"))
O = int(input("skriv inn et til tall"))
def f(x):
    return u*x+O

e=0
a = 1000
b = -1000

"""
while e <1000:
    
    if f(a)>0 and f(b)<0:
        c = (a+b)/2
        if f(c)==0:
            print(c)
            break
        elif f(c)>0:
            a=c
            e+=1
        elif f(c)<0:
            b=c
            e+=1
"""
print(f(1))

while e<1000000:
    c = (a+b)/2
    if f(c)==0 or f(c) == 0.0001:
        print(c)
        break
    elif f(c)>0:
        a=c
        e+=1
        print("hu")
    elif f(c)<0:
        b=c
        e+=1
        print("lmk")
        