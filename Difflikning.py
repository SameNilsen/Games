# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 10:24:55 2019

@author: MortenNilsen
"""
from pylab import *
år = 1
måneder = år*12
p_0 = 40
k = 0.05
liste = []
tid = [0]
liste.append(p_0)


for i in range(måneder):
    p_0=p_0*(1+k)
    liste.append(p_0)
    tid.append(i+1)
    
print(p_0)

x1 = tid
y1 = liste
plot(x1, y1, 'm.')
xlabel('Måneder')
ylabel('Aper')
grid('on')
show()