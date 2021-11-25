
"""
Solflekker

"""

import pylab as pl


data = pl.loadtxt('solflekker.txt')

"""
måned = data[:, 0]
solflekker = data[:, 1]
pl.plot(måned, solflekker)
print(data[3, 1]*data[4, 1])

a = [1, 3, 4]
c = [3, 5, 7]
b = pl.array(a)
d = pl.array(c)
print(b*d)
"""
"""
liste1 = []
for i in range(0, 6):
    liste1.append(data[i,:])
print(liste1)

liste2 = []
e=0
while e<6:
    liste1.append(data[e,:])
    e+=1
    print(liste2)
"""
matrise = pl.zeros(10, int)
print(matrise)
matrise[2] = 5
print(matrise)