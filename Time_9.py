"""
Plotting
"""
"""
from pylab import *
def f(x):
    return sin(x)
def g(x):
    return cos(x)
def h(x):
    return tan(x)

x = linspace(0, 10, 100)   #lager matrise
y1 = f(x)                 #lager matrise av matrise
y2 = g(x)
y3 = h(x)

xlabel('x')
ylabel('f(x)')
title('Vårt første plott')
plot(x, y1, 'm--')
plot(x, y2, 'g--')
plot(x, y3, 'k--')
grid('on')
show()
"""
from pylab import *
def w(x):
    return 5*x-1
x = linspace(0, 10, 10)
y4 = w(x)
plot(x, y4)

