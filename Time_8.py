# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:06:17 2018

@author: MortenNilsen

from pylab import *
tall = [1, 2, 3, 4]
tall2 = [5, 6, 7, 8]
matrise1 = array(tall)
matrise2 = array(tall2)
print(matrise1 + matrise2)

liste = [1, 2, 3, 4, 5]

for i in range(len(liste)):
    print(liste[i])
    
for tall in liste:
    print(tall)

#Tuppel

tuppel = (1, 2, 3)
tuppel.pop(1)


fotballspillere = ("Messi", "Ronaldo", "Zlatan", "Jarstein", "Hazard", "Isco", "Miranda", "Negredo", "Rodrigo", "Navas")

for i in range(0,len(fotballspillere),2):
    print(fotballspillere[i])
"""

from pylab import *
liste = [1, 2, 3, 4, 5, 6, 8, 7]
c = array(liste)
#print(max(liste))
b = c / 2

print(b)

for i in range(b):
    if i is float:
        print("heii")
    elif i is int:
        print("jjj")

"""
for i in range(len(liste)):
    if (liste[i] % 2):
        liste.pop(i)
    else:
        print("heu")
        
for element in b:
    if element is float:
        print("heii")
    elif element is int:
        print("tull")
"""

    
        