# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:39:19 2019

@author: MortenNilsen
"""
#Oppgave 4

from pylab import *

def f(x):
    return x**3 - 2*x + 1

def g(x):
    e = 2.718
    return e**x

u = -2.5
while u < 5:
    tol = 0.001
    if f(u)==g(u):
        print(u)
    elif abs(f(u)-g(u))<tol:
        print(u)
    u += 0.001
"""
Her har jeg prøvd å la maskinen prøve så mange som mulige tall mellom -2.5 og 5 siden jeg ser at det er mellom der
de krysser hverandre. Så prøver jeg først å sjekke om jeg på mirakuløst vis klarer å finne akkurat der de krysser
ved linje 21. Men siden det mest sannysnlig ikke funker, prøver jeg å finne ut om det som skiller dem er mindre
enn toleransen jeg har satt. For hver gang løkka kjører legger jeg på litt på u verdien for at den skal sjekke 
så mange mulige verdier som mulig
Om du endrer på toleransen og u kan du få mye forskjellige svar. blant annet om du tar en lav toleranse, vil du få 
mange svar, siden den tolererer mye. Jeg har derfor valgt å si meg fornøyd med de verdienen jeg valgte her.
"""


ylim(-50, 100)
y1 = f(x)
y2 = g(x)
plot(x, y1, 'm')
plot(x, y2, 'b')
grid('on')
show()
"""
Her plotter jeg grafen for å se cirka hvor skjæringen er
"""


