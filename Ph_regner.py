# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 09:59:08 2018

@author: MortenNilsen
"""


from pylab import *                                                             #må importere pylab for å bruke funksjonen "log"

h = float(input("konsetrasjon av H3o+ oksoniumioner gitt i mol per liter\n"))   #ber brukeren oppgi konsentrasjonen av oksoniumioner, setter det som float for å fp med deismaltall

def f(h):
    return -log(h)                                                              #definerer en funksjon der h er konsentrasjonen

print("ph'en gitt mengde oksoniumioner gitt i mol per liter er", f(h))          #printer ut resultatet med litt tekst



                