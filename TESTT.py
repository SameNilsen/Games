# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 20:17:22 2018

@author: MortenNilsen
"""

liste=[]
liste.append(1)

n = int(input("Til hvilket tall ønsker du å sjekke, fra 1\n"))
for i in range(2,n+1):
    m=0
    for g in range(2,i):
        if i%g == 0:
                m=1
    if not m==1:
        liste.append(i-1)
    elif m==1:
        for dele in range(2,i):
            dele2 = i/dele
            if dele2%1 == 0:
                dele2=int(dele2)
                if i%dele == 0:
                    if not dele2%dele == 0:
                        liste.append(liste[dele-1]*liste[dele2-1])
                        break
                    else:
                        liste.append(dele*liste[dele2-1])
                        break 

def a():
    print("\n")
    for l in range(1,len(liste)+1):
        print(l, liste[l-1])

def b():
    b = int(input("Hva ønsker du at n skal være\n"))
    print("\n")
    print(b,liste[b-1])
    
def c():
    fra = int(input("Hvilket tall ønsker du å se fra?\n"))
    til = int(input("Til og med hviket tall?\n"))
    print("\n")
    for p in range(fra,til+1):
        print(p,liste[p-1])                        
                        
valg = int(input("Hva ønsker du å se, av tallene du har sjekket?\n1.En liste med alle verdiene\n2.En enkel verdi\n3.Fra en verdi til en annen\n"))
if valg == 1:
    a()
elif valg == 2:
    b()
elif valg == 3:
    c()