# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:23:38 2018

@author: MortenNilsen
"""

import pandas as pd

Tall = pd.read_csv("Tall.csv",sep = ";", encoding = "ISO-8859-1")

print(Tall.head())


