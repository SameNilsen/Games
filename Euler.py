# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:16:37 2018

@author: MortenNilsen
"""
n=24
k=0
m=0
p=0
for i in range(1,n+1):
    if n%i==0:
        print("Bra", k)
        k+=1 
    if not n%i==0:
        print("Nei", m)
        for u in range(2, n):
                if not i%u == 0:
                    for a in range(2, n):
                        if i%a == 0:
                            p+=1
                            break
                    if p ==1:
                        break
                    else:
                        m+=1
                    break 
print("m:", m, "k:", k)
    