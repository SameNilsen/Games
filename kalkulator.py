# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 20:58:03 2018

@author: MortenNilsen
"""

from math import *


Svar_1 = str(input("Er ditt problem et matte spørsmål?"))

if Svar_1 == "ja":
    Svar_2 = str(input("Er det et enkelt regnestykker eller en andregradsfunksjon?"))
    if Svar_2 == "enkelt regnestykke" or Svar_2 == "1":
        A = float(input("skriv inn tall A:"))
        C = input("regneoperasjon:")
        B = float(input("skriv inn tall B:"))
        if C is "+":
            print(A + B)
        elif C is "-":
            print(A - B)
        elif C is "*":
            print(A * B)
        elif C is "/":
            d = (A/B)
            print(d)
        else:
            print("det blir for komplisert")
    elif Svar_2 == "andregradsfunksjon" or Svar_2 == "2":
        a = float(input("Skriv inn a:"))
        b = float(input("skriv inn b:"))
        c = float(input("skriv inn c:"))
        print("\n")
        Produkt_0 = ((b)**2 -4*a*c)
        
        if a == 0:
            print("NEI! a kan ikke være 0")
        elif a > 0:
            if Produkt_0 > 0:
                print("det blir to løsninger")
                løsning = (-1*(b) + sqrt((b)**2 -4*a*c))/(2*(a))
                løsning_2 = (-1*(b) - sqrt((b)**2 -4*a*c))/(2*(a))
                print("Løsningene blir:", løsning, "og", løsning_2)
            elif Produkt_0 == 0:
                print("det blir en løsning")
                løsning = (-1*(b) + sqrt((b)**2 -4*a*c))/(2*(a))
                løsning_2 = (-1*(b) - sqrt((b)**2 -4*a*c))/(2*(a))
                print("Løsningene blir:", løsning, "og", løsning_2)
            else:
                print("det blir ingen løsninger")
        else:
            if Produkt_0 > 0:
                print("det blir to løsninger")
                løsning = (-1*(b) + sqrt((b)**2 -4*a*c))/(2*(a))
                løsning_2 = (-1*(b) - sqrt((b)**2 -4*a*c))/(2*(a))
                print("Løsningene blir:", løsning, "og", løsning_2)
            elif Produkt_0 == 0:
                print("det blir en løsning")
                løsning = (-1*(b) + sqrt((b)**2 -4*a*c))/(2*(a))
                løsning_2 = (-1*(b) - sqrt((b)**2 -4*a*c))/(2*(a))
                print("Løsningene blir:", løsning, "og", løsning_2)
            else:
                print("det blir ingen løsninger")   
        if a == 1:
            if b == 1:
                if c == 1:
                    print("Likningen blir: x^2 +", "x + 1")
                elif c == 0:
                    print("likningen blir: x^2 + x")
                else:
                    print("Likningen blir: x^2 + x +", c)
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
    else:
        print("hæ")
elif Svar_1 == "nei":
    print("Da kan jeg ikke hjelpe deg")
else:
    print("hæ")
    
    
    
    
    
    

    


