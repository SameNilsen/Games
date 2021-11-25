# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:51:57 2019

@author: MortenNilsen
"""
#Oppgae 5


tid = [0, 15, 25, 45, 60, 90]
Blodsukker = [5.2, 6.5, 7.8, 6.5, 5.4, 5.3]
Akselerasjon = []

for i in range(0, len(Blodsukker)):
    Akselerasjon.append((Blodsukker[i]-Blodsukker[i-1])/(tid[i]-tid[i-1]))

x1 = tid
y1 = Blodsukker
x2 = tid
y2 = Akselerasjon
plot(x1, y1, 'm.')
plot(x2, y2, 'b')
xlabel('minutter')
ylabel('Blodsukker')
grid('on')
show()
"""
Resultater:
Vi ser at Blodsukkeret går opp på starten etter at han har spist eplet, før det går ned igjen. 
Vi ser også ut ifra den deriverte eller endringen, at blodsukkernivået stiger rundt 20 minutter og at der er økningen positiv
mens etter det går det nedover igjen
"""

