# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:16:32 2019

@author: MortenNilsen
"""
def f(x):
    return x**2

def der(f, x, h):
    return (f(x+h)-f(x))/h

print(der(f, 2, 1E-8))


"""
for linje in fil:
    data = linje.split(',')
    print(data)
    tid.append(float(data[0]))
    fart.append(((float(data[1])+h)-float(data[1]))/h)
"""




