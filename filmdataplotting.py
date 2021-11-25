# -*- coding: utf-8 -*-
"""
Frokostblandinger
"""

import pandas as pd

data = pd.read_csv('filmdata.csv', sep = ";", encoding = "ISO-8859-1") 
print(data)
