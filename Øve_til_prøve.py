# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 13:15:32 2018

@author: MortenNilsen
"""



"""
Dyr = ["stubbneseape", "bladsjøhest", "sjøkneler", "gaupe",
"axolotl", "blobfisk", "bjørnedyr", "dovendyr"]
for i in range(1,5,2):
    del Dyr[i]
print(Dyr)

Cliste = []

F = 0

for i in range(0, 41):
    Cliste.append((F-32)*5.0/9)
    F += 5
print(Cliste)

Liste1 = []
Liste2 = []
p = 1
while p<11:
    Liste1.append(2*p)
    p += 1
print(Liste1)
e = 0
while e<10:
    Liste2.append((2*e)+1)
    e += 1
print(Liste2)


s = int(input("start"))
d = s + 11

for i in range(s, d):
    Liste1.append(s*2)
    s += 1

partall = []
oddetall = []
for i in range(0,10):
    partall.append(2*i)
    oddetall.append(2*i+1)
print(partall, oddetall)

O = int(input("Hva er den observerte bølgelengden?"))
L = int(input("hva er laboratorie bølgelngden?"))
c = 3*(10**8)

def v(O, L):
    return ((O-L)*c)/L
if v(O, L) < 0:
    print("Stjernen er blåforskyvet, altså den går bort ifra oss. Farten er", v(O, L))
else:
    print("Stjernen er rødforskyvet, altså den kommet mot oss")

y = 1
for i in range(10):
    for u in range(2):
        print(y)
        y += 1
    y += 2    

def f(x):
    return x**2
print(f(2))

print(4==3)
print(f(2)==4)

t = int(input("hva er tiden?"))
v = int(input("hva er farten?"))
print("da er strekningen", v*t )

def s(t, v):
    return t*v
"""
e = 0
liste=[]

while e<497:
    liste.append(e)
    e = 2*e+1
print(liste)



    