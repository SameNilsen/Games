# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:08:15 2018

@author: MortenNilsen
"""
"""
for i in range(2, 18,):
    print(i*2)


while i > 15:
    i += 2
    print(i*3)

n = 10
for i in range(0, n, 1):
    print("hei"*i)
"""
"""
import random


fra = int(input("skriv inn fra hvilket tall"))
til = int(input("til hvilket tall"))
x = random.randint(fra, til)
forsøk = 0
a = int(input("gjett et tall mellom"))

while a<x:
    print("tallet er for lite")
    a = int(input("gjett på nytt\n"))
    forsøk += 1
    while a>x:
        print("tallet er for stort")
        a = int(input("gjett på nytt\n"))
        forsøk += 1
while a>x:
    print("tallet er for stort")
    a = int(input("gjett på nytt\n"))
    forsøk += 1
    while a<x:
        print("tallet er for lite")
        a = int(input("gjett på nytt\n"))
        forsøk += 1
if a == x:
    print("riktig, du brukte:", forsøk + 1, "forsøk")

word = ""

for i in range(1):
    word+="A"
    for j in range (2):
        word+="b"
    for k in range (1):
        word+="a"
    
print(word)
"""
"""
for i in range(101):
    print(i)

for i in range(50, 76):
    print(i)

for i in range(0, 100, 2):
    print(i)

skryt = 0
a = int(input("skriv inn hvor mange ganger"))
while skryt < a:
    print("du er flink")
    skryt += 1

i = 1
while i < 51:
    print(i)
    i += 1

    
i = 50
while i < 100:
    print(i*2)
    i += 1

from math import *
i = 0
while i < 101:
    print(i, sqrt(i))
    i += 1

N = 10000000000
rekkesum = 0
for n in range(1, N):
    rekkesum += (1/n**2)
print(rekkesum)
"""

h = 6.63*(10**-34)
B = 2.18*(10**-18)

n = float(input("skriv inn skall n:"))
m = float(input("skriv inn skall m:"))

f = (B/h)*((1/m**2)-(1/n**2))

#print(f)

b = 3*10**8/f
print(b)
"""
h = 6.63*(10**-34)     #Plancks konsant

B = 2.18*(10**-18)     #Bohrs konstant

c = 3E8                #Lysets hastighet

tall = int(input("skriv inn fra hvilket skall"))

r = tall-1

for r in range(tall, 1, -1):
    r -= 1
    f = (B/h)*((1/r**2)-(1/tall**2))
    b = c/f
    print(b*10**9)
"""
    
    
