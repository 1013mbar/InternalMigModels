# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:34:48 2020

@author: lucas
"""

import pandas as pd

data  = pd.read_csv('alabamaData.csv', ',',dtype = {'fipsA': 'str', 'fipsB': 'str'})
fipsA = data['fipsA'].values
fipsB = data['fipsB'].values
for i in range(len(fipsA)):
    fipsA[i] = (fipsA[i])[1:]
    fipsB[i] = (fipsB[i])[1:]
data['fipsA'] = fipsA
data['fipsB'] = fipsB
data.to_csv('alabamaData.csv')