# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:51:57 2019

@author: MortenNilsen
"""
from pylab import *

def f(x):
    return x**3 - 2*x + 1

def g(x):
    e = 2.718
    return e**x
"""
for i in range(1,7, 1000):
    if f(i)==g(i):
        print(i)
"""
u = -2.5
while u < 5:
    tol = 0.001
    if f(u)==g(u):
        print(u)
    elif abs(f(u)-g(u))<tol:
        print(u)
    u += 0.001

x = linspace(-10, 10, 100)
y = linspace(-10, 10, 100)
ylim(-50, 100)
y1 = f(x)
y2 = g(x)
plot(x, y1, 'm')
plot(x, y2, 'b')
xlabel('minutter')
ylabel('Blodsukker')
grid('on')
show()

