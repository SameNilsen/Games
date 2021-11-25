# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 08:52:51 2018

@author: MortenNilsen
"""
"""
navn = input("hva heter du?")
print ("hei:", navn)
alder = input("hvor gammel er du?") 
print ("wow", navn, ", er du", alder, "år gammel?")
"""
"""
år = int(input("skriv inn år"))

sek = år*365*24*60*60

print ("det er", sek, "sekunder i", år, "år")
"""

#definsjoner

def f(x):
    return x**2-2*x+1

#kalle funksjonen
y=f(3)

print(y)

print(f(1), f(2))
"""
æ = 10                      #antall ganger du vil få ut "noe" 

def noe(æ):
    print(æ*"du er kul ")
    return;

noe(æ)

a = input("hvor gammel er du?")
b = input("hva heter du?")

def hei():
    print()
"""
from math import pi                 #3.7
"""
a = int(input("skriv inn radius"))
print (a**2 * pi)

b = int(input("skriv inn radius"))
print ("volumet av en kule med radius", b, "er:", 4/3 * b**3 )
"""
"""
def t_f_til_c(f):
    amount = f - 32 * 5/9
    print(amount)
    
t_f_til_c(100)


v = int(input("hva er hvilepulsen din?"))
v_2 = int(input("hva er makspulsen din?"))
v_3 = int(input("hva er intensiteten din"))

N = int(v_2 - v)

print("da er pulsen din nå", N * v_3 + v, "slag per minutt")
"""
"""
SurSild = int(16)
MelkeSjokolade = int(25)
PotetGull = int(20.5)

a = input("hva vil du ha")
b = int(input("hvor mye penger har du?"))

if a is "S":
    print(b/SurSild)
else:
    print("hei")
"""
i = 3
for i in range(101):
    print(i)












    
    

    
