# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 09:31:29 2018

@author: MortenNilsen
"""
from pylab import *     #vi bruker sqrt så trenger å importere pylab biblioteket


print(" tid = t \n akselerasjon = a \n sluttfart = v \n startfart = v_0 \n strekning = s")                 #starter med å vise brukeren forkortelser
spørsmål_1 = str(input("hvilken verdi vil du ha?"))                                                        #spør hva brukeren vil ha

if spørsmål_1 == "s":                                                                                      #vi har to formler for s og to formler for v, så deler inn i hva brukeren vil ha først. 
    spørsmål_2 = str(input("hvilke verdier har du fra før av? Skriv det i samme rekkefølge som øverst:"))  #kunne ha tatt alle muligheter for å kombinere rekkefølgen på verdiene, men valgte å spesifisere.
    if spørsmål_2 == "t, a, v_0":
        t = float(input("skriv inn tid"))
        a = float(input("skriv inn akselerasjon"))
        v_0 = float(input("skriv inn startfart"))
        def s_1(t, a, v_0):                                                                                #definerer formelen og bruker verdiene som ble spurt etter
            return (1/2)*a*t**2+v_0*t                                                                      #førse strekningsformel 
        print(s_1(t, a, v_0), "meter")
    elif spørsmål_2 == "t, v, v_0":                                                                        #hvis man vil ha s, men man har litt andre verdier, blir andre formel brukt
        t = float(input("skriv inn tid"))
        v = float(input("skriv inn sluttfart"))
        v_0 = float(input("skriv inn startfart"))
        def s_2(t, v, v_0):
            return (1/2)*(v_0+v)*t                                                                         #andre strekningsformel
        print(s_2(t, v, v_0), "meter")
elif spørsmål_1 == "v":                                                                                    #samme oppsett, bare for v
    spørsmål_2 = str(input("hvilke verdier har du fra før av? Skriv det i samme rekkefølge som øverst:"))
    if spørsmål_2 == "t, a, v_0":
        t = float(input("skriv inn tid"))
        a = float(input("skriv inn akselerasjon"))
        v_0 = float(input("skriv inn startfart"))
        def v_1(t, a, v_0):                                                                                #første fartsformel
            return a*t+v_0
        print(v_1(t, a, v_0), "m/s")
    elif spørsmål_2 == "a, v_0, s":
        a = float(input("skriv inn akselereasjon"))
        v_0 = float(input("skriv inn startfart"))
        s = float(input("skriv inn strekning"))
        def v_2(a, v_0, s):
            return sqrt((v_0**2)+(2*a*s))                                                                  #den tidløse formelen
        print(v_2(a, v_0, s), "m/s")
        
        
        
    
        
    


