# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 09:59:08 2018

@author: MortenNilsen
"""


from pylab import *

h = float(input("antall mol per liter"))

def f(h):
    return -log(h)

print("ph'en gitt mengde oksoniumioner gitt i mol per liter er", f(h))






                