# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 10:06:18 2018

@author: MortenNilsen
"""
"""
navn = str(input("hva heter du?"))

if navn == "Morten" or navn == "morten":
    print("Bra")
elif navn == "Sigurd" or navn == "sigurd":
    print("Ikke bra")
else:
    print("greit nok")
"""


"""
a = str(input("skriv inn hva\n"))
b = int(input("Hvor mange ganger?\n"))

for i in range(b):
    print(a)

for i in range(5, 17):
    print(i)

for i in range(100):
    print(i*2)

for i in range(50):
    print((i*2)+1)

from math import *
for i in range(50):
    print(sqrt(i))

fakultet = 1
for i in range(1, 53):
    fakultet = fakultet*i
print(fakultet)
   
for i in range(100):
    print("a"*i)
"""
from PIL import Image, ImageDraw

img = Image.new('RGB', (130, 200), color=(1, 4, 146))

d = ImageDraw.Draw(img)
d.line((31, 175) + (61, 49), fill=(228, 72, 5))

img.save('Bildee.png')

