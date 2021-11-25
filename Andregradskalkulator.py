# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 10:02:16 2018

@author: MortenNilsen
"""

#Jeg lagde egentlig dette programmet for en stund siden, så den delen som skriver ut likningen er-
#-gammel og dårlig skrevet, men jeg tenkte at jeg kunne la den være med.
#selve kalkulatoren har jeg oppdatert slik at den passer oppgaven, i utgangspunket var det bare-
#-masse if-elif-else linjer.

from math import *                          #importerer pylab fordi vi skal kunne bruke sqrt 

a = float(input("Skriv inn a:"))            #a, b og c verdier som vi skal bruke videre
b = float(input("skriv inn b:"))
c = float(input("skriv inn c:"))
print("\n")                                 #for å skape struktur

Produkt_0 = ((b)**2 -4*a*c)                 #lager en variabel for å sjekke om det inni kvadratroten-
                                            #-er mindre, lik eller mer enn null(det gir jo forskjellige-
                                            #-antall løsninger)




if a == 0:                                                           #a kan ikke være 0, så vi lager en-
    print("NEI! a kan ikke være 0")                                  #-egen linje for det

elif a > 0 or a <0:                                                  #for alle andre vedier for a:
    if Produkt_0 > 0:                                                #hvis det inni kvadratroten-
        print("det blir to løsninger")                               #- er mer enn 0 blir det to løsninger
        def f(a, b, c):                                              #definerer formelen
            return (-1*(b) + sqrt((b)**2 -4*a*c))/(2*(a))
        def f_2(a, b, c):                                            #blir to løsninger, så definerer to
            return (-1*(b) - sqrt((b)**2 -4*a*c))/(2*(a))
        print("løsningene blir:", f(a, b, c), "og", f_2(a, b, c))
    elif Produkt_0 == 0:                                             #hvis det inni kvadratroten blir-
        print("det blir en løsning")                                 #-lik null, blir det én løsning
        def f(a, b):                                                 #definerer igjen, bare at her blir-
            return (-1*b)/(2*a)                                      #-det ingenting som skal +/- med -1*b
        print("løsningen blir:", f(a, b))
    else:                                                            #det går ikke an å a kvadratroten av-
        print("det blir ingen løsninger")                            #et negativt tall
    
if a == 1:                                                           #det herifra og nedover lagde jeg når vi lærte-
    if b == 1:                                                       #om if-elif-else første gang, så jeg bare lekte meg litt
        if c == 1:
            print("Likningen blir: x^2 +", "x + 1")
        elif c == 0:
            print("likningen blir: x^2 + x")
        elif c > 1:
            print("Likningen blir: x^2 + x +", c)
        else:
            print("Likningen blir: x^2 + x", c)
    elif b == 0:
        if c == 1:
            print("likningen blir: x^2 + 1")
        elif c == 0:
            print("likningen blir: x^2")
        else:
            print("likningen blir: x^2 +", c)
    else:
        if c == 1:
            print("Likningen blir: x^2 +", b,"x + 1")
        elif c == 0:
            print("likningen blir: x^2 +", b,"x")
        else:
            print("Likningen blir: x^2 +", b,"x +", c)
elif a == 0:
    print("derfor blir det ikke en andregrads likning")
else:
    if b == 1:
        if c == 1:
            print("Likningen blir:", a, "x^2 + x + 1")
        elif c == 0:
            print("likningen blir:", a, "x^2 + x")
        else:
            print("Likningen blir:", a,"x^2 + x +", c)
    elif b == 0:
        if c == 1:
            print("Likningen blir:", a, "x^2 +1")
        elif c == 0:
            print("likningen blir:", a, "x^2")
        else:
            print("Likningen blir:", a,"x^2 +", c)
    else:
        if c == 1:
            print("Likningen blir:", a, "x^2 +", b,"x + 1")
        elif c == 0:
            print("likningen blir:", a, "x^2 +", b, "x")
        else:
            print("Likningen blir:", a,"x^2 +", b,"x +", c)
            


    













    
    
    


