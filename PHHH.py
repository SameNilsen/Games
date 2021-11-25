#pH regner

from math import *  
from pylab import *
import pandas as pd


data = pd.read_csv('Stoffer.csv', sep = ";", encoding = "ISO-8859-1") 
print(data)

u=0
jj = input("Er det en sterk syre eller base? :")
if jj == "sterk syre":
    u += 1
elif jj == "sterk base":
    u += 2
elif jj == "nei":
    j = input("Er løsningen på lista? :")
    if j == "ja":    
        pp = input("Syre eller base? :")
        if pp == "syre":
            s = float(input("Hvilken syre? :"))
            b = float(data['Ka'][s])
            print("Syrekonstanten er: ", b)
        elif pp == "base":
            s = float(input("Hvilken korresponderende syre(Ka)? :"))
            b = (10**(-14))/data['Ka'][s]
            print("(10**-14)/Ka:")
            print("Basekonstanten er: ", b)
    elif j == "nei":
            y = input("syre eller base? :")
            print("---------")
            if y == "syre":
                print("SyreKonstant(a*10**(-b)):")
                jjjj = float(input("a="))
                jjjjj = float(input("b="))
                b = jjjj*10**(-jjjjj)
                print("=", b)
            elif y == "base":
                print("Syrekonstant til korresponderende syre(a*10**(-b)):")
                jjjj = float(input("a="))
                jjjjj = float(input("b="))
                print("Ka=", jjjj*10**(-jjjjj))
                print("Kb = Kw/Ka = 10**(-14) /", jjjj*10**(-jjjjj))
                b = (10**(-14))/(jjjj*10**(-jjjjj))
                print("Kb=", b)

print("---------")   
ppp = str(input("Hva har du? n, v, c, m :"))
if ppp == "n":
    n = float(input("Stoffmengde(n)="))
    v = float(input("Volum(v)="))
    print("c = n/v =", n, "/", v)
    kons = n/v
    print("Konsentrasjon(c)= ", kons)
elif ppp == "m" or ppp == "v":
    m = float(input("Masse="))
    if j == "nei":
        print("Molarmasse beregning:\n")
        Mm = 0
        k = 1
        for i in range(100):
            print(k)
            a = input("Grunnstoff:")
            if a == "c":
                g = float(input("Hvor mange:"))
                Mm += g*12
            elif a == "h":
                g = float(input("Hvor mange:"))
                Mm += g*1
            elif a == "he":
                g = float(input("Hvor mange:"))
                Mm += g*4
            elif a == "na":
                g = float(input("Hvor mange:"))
                Mm += g*23
            elif a == "n":
                g = float(input("Hvor mange:"))
                Mm += g*14
            elif a == "o":
                g = float(input("Hvor mange:"))
                Mm += g*16
            elif a == "cl":
                g = float(input("Hvor mange:"))
                Mm += g*35.45
            elif a == "b":
                g = float(input("Hvor mange:"))
                Mm += g*10.8
            elif a == "p":
                g = float(input("Hvor mange:"))
                Mm += g*31
            elif a == "s":
                g = float(input("Hvor mange:"))
                Mm += g*32
            elif a == "f":
                g = float(input("Hvor mange:"))
                Mm += g*19
            elif a == "e":
                break
            k += 1
    elif j == "ja":
        Mm = data['Mm'][s]
    Mm = float(Mm)
    print("Molarmasse(Mm) = ", Mm)
    print("n = m/Mm =", m, "/", Mm)
    n = m/Mm
    print("Stoffmengde(n) = ", n)
    v = float(input("Volum(v)="))
    kons = float(n/v)
    print("c = n/v =", n, "/", v)
    print("Konsentrasjon(c)=", kons)
elif ppp == "c":
    kons = float(input("Konsentrasjon="))
print("---------")

if u == 1:
    print("PH = -log10(x) = ", -log10(kons))
elif u == 2:
    print("PH = 14-(-log10(x)) = ", 14-(-log10(kons)))
else:
    c = float(b*kons*-1)
    print("\n")
    x_1 = (-1*(b) + sqrt((b)**2 -4*c))/2
    x_2 = (-1*(b) - sqrt((b)**2 -4*c))/2  
    if pp == "syre":
        print("Ka = x**2 / (c-x)")
        print("x**2 + Ka*x - Ka*c")
        print("x=", x_1)  
        print("PH = -log10(x) = ", -log10(x_1))
    elif pp == "base":
        print("Kb = x**2 / (c-x)")
        print("x**2 + Kb*x - Kb*c")
        print("x=", x_1)  
        print("PH = 14-(-log10(x)) = ", 14-(-log10(x_1)))    

#0.00261
#0.00020833333