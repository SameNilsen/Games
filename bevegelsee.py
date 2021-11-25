# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:52:28 2019

@author: MortenNilsen
"""
from pylab import *

tid = []
fart = []
akselerasjon = []
fil = open('Bevegelse.txt', 'r')


for linje in fil:
    data = linje.split(',')
    print(data)
    tid.append(float(data[0]))
    fart.append(float(data[1]))
    
fil.close()

x1 = tid
y1 = fart


for i in range(0, len(fart)):
    akselerasjon.append((fart[i]-fart[i-1])/(tid[i]-tid[i-1]))
    
x2 = tid
y2 = akselerasjon
plot(x1, y1)
plot(x2, y2)
grid('on')
show()




    