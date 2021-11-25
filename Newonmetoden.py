# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:08:54 2019

@author: MortenNilsen
"""

a = -5
tol = 1E-15
c = a
i = 0

from pylab import *

def f(x):
    return x**2-2*x-2

def g(x):
    return 2*x-2
    
def Newtonmetoden(f, g, a, tol = 1E-15):
    c = a
    i = 0
    while abs(f(c)) > tol:
        c = a - f(a)/g(a)
        a = c
        i += 1
    print("nullpunktet er", c, " og løkka kjørte:", i, "ganger")
    return c

x = linspace(-10, 10, 100)
y1 = f(x)
plot(x, y1)
grid('on')
show()

p = input("Er det en lineær graf?")
if p == "ja":
    u = float(input("Velg punkt"))
    Newtonmetoden(f, g, u)
elif p == "nei":
    u = float(input("Velg punkt"))
    Newtonmetoden(f, g, u)
    k = float(input("Velg punkt"))
    Newtonmetoden(f, g, k)