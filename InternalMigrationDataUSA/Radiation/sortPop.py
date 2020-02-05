# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:54:22 2020

@author: lucas
"""


import pandas as pd
import numpy as np

data1 = pd.read_csv('../../../Data/countyPop2014_v3.csv',',',dtype = {'county': 'str'})
data2 = pd.read_csv('../../../Data/sf12010countydistancemiles.csv',',',dtype = {'county1': 'str', 'county2': 'str'})
countyCode = "01125"



countyTPop = (data1.iloc[np.where(data1.county.values==countyCode)])['population'].values[0]
countyDist = data2.loc[data2['county1'] == countyCode]
countyDist = countyDist.sort_values('mi_to_county')
destCode = np.array(countyDist['county2'])
destDist = np.array(countyDist['mi_to_county'])

popCodes = np.array(data1['county'])
popPop = np.array(data1['population'])

sortedPop =[]
sortedCodes = []
newDist = []
for i in range(len(destCode)):
    for j in range(len(popCodes)):
        if(destCode[i] == popCodes[j]):
            sortedPop.append(popPop[j])
            sortedCodes.append(popCodes[j])
            newDist.append(destDist[i])
    print(i)

df = pd.DataFrame()
df['fips'] = sortedCodes
df['population'] = sortedPop
df['dist'] = newDist
print(df)
df.to_csv('sortedPop_'+ countyCode +'.csv')