# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 09:30:38 2018

@author: MortenNilsen
"""

T = int(input("antall tøffeldyr du vil starte med"))    
T_1 = T                                                #når vi skal printe ut svarteksten, vil vi ha en T for det- 
                                                       #-i tastet inn først og de vi fikk til slutt
t = int(input("antall timer:"))    

for i in range(1, t, 2):                  #se nederst
    T_1 += T_1                            #dobler seg selv hver gang
    
print("antall tøffeldyr etter", t, "timer er", T_1, "hvis man begynner med", T, "tøffeldyr" )

#hver andre time, så to steg. den må starte på 1 fordi hvis den starter på 0 og man skriver t = 1, vil-
#-den lese 0, 2, 4, 6... så da vil den lese fra 0 til 0, og vil doble seg selv ved 1time. tar man derimot-
#-at den starter på 1 og t = 1, vil den lese 1, 3, 5, 7... og lese fra 1 til 0 ved 1time og dermed ikke-
#-printe ut noe på første "runde".