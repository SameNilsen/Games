# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:10:50 2018

@author: MortenNilsen
"""
"""
Skiløpere = ["Marit Bjørgen", "Therese Dophaug", "Petter Northug", "Emil Trynersen", "Heidi Weng"]
SjakkSpillere = ["Magnus Carlsen", "Vishvatnan Annan", "Sergei Kariakin", "Ho Gi Faen", "Nakamura"]

NoenIdrettsFolkOgNoenTenkere = Skiløpere + SjakkSpillere
NoenIdrettsFolkOgNoenTenkere.pop(1)
NoenIdrettsFolkOgNoenTenkere.pop(3)
a = NoenIdrettsFolkOgNoenTenkere.index("Nakamura")
print(NoenIdrettsFolkOgNoenTenkere[2:6].pop(3))

Liste = [1]
n = 1
for i in range(0, 1000):
    Liste.append(2**n)
    n += 1
print(Liste)
"""
liste = ["dette", "er", "en", "ganske", "lang", "liste", "med", "ikke", "Så", "viktig", "innhold"]
liste2 = liste[:3] + liste[5:7] + liste[9:]  
print(liste2)