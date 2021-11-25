# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:46:57 2019

@author: MortenNilsen
"""
from pylab import *

fil = imread('BILDE.png')
print(fil)
#imshow(fil)

NyttBilde = []
"""
for i in range(0, len(fil)):
    NyttBilde.append(fil[i,i,:]-fil[i,i+1,:])
    for u in range(3):
"""

NYY = abs(fil[1:-1, 2:, :] - fil[1:-1,1:-1,:])
imshow(3*NYY)
show

NYYY = abs(fil[2:, 1:-1, :] - fil[1:-1,1:-1,:])
imshow(3*NYYY)
show

grad = sqrt(NYY**2 + NYYY**2)
imshow(3*grad)
