# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:28:11 2019

@author: MortenNilsen
"""
from pylab import *

def f(x):
    return x**3 + 3*x**2

x = linspace(-10, 10, 100)
y1 = f(x)
plot(x, y1)
grid("on")
show()


def Halveringsmetoden(f, a, b, feil = 1E-8):
    c = (a+b)/2
    t=1
    while abs(f(c)) > feil:
        if f(c)*f(a) < 0:
            b=c
        elif f(c)*f(b) < 0:
            a=c         
        c = (a+b)/2
        t += 1
    print("Løsninga er x=",c,"og løkka kjørte", t, "ganger")

u = float(input("Startverdi"))
o = float(input("Sluttverdi"))  
    
Halveringsmetoden(f, u, o)




    

