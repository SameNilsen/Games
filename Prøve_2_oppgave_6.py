# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:35:24 2019

@author: MortenNilsen
"""

#Oppgave 6

timer = 15
p_0 = 1000
k = 0.62
liste = []
tid = [0]
liste.append(p_0)


for i in range(timer):
    p_0=p_0*(1+k)
    liste.append(p_0)
    tid.append(i+1)

x1 = tid
y1 = liste
plot(x1, y1, 'm.')
xlabel('Timer')
ylabel('Bakterier')
grid('on')
show()

print("Bakterie poupulasjon etter", timer, "timer er:", p_0)

"""
Resultater:
Vi ser at det er 1 389 073 bakterier etter femten timer, som betyr at det har steget raskt. Og utifra grafen ser vi at
det blir bare mer og mer. 
De biologiske forutsetningene vi må ta er at det ikke skjer noe med populasjonen annet enn formering. Da tenker jeg på 
ytre faktorer som kan drepe bakteriene.
"""