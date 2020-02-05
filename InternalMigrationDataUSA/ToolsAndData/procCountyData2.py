# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 07:54:26 2020

@author: lucas
"""
import pandas as pd
import numpy as np



def calcCountyMig(countyCode,noCounties,countyCodeAr,countyDist,countyTPop,countyPopAr):
    moveAr = []
    for i in range(noCounties):
        if countyCodeAr[i] != countyCode:
            dist = countyDist.loc[countyDist['county2'] == countyCodeAr[i]]['mi_to_county'].values[0]
            moveAr.append(migFlow(countyTPop,countyPopAr[i],dist))
    return moveAr

def migFlow(pop1,pop2,distance):
    return((pop1*pop2)/distance)

data1 = pd.read_csv('../../../Data/countyPop2014_v2.csv',' ')
data2 = pd.read_csv('../../../Data/sf12010countydistancemiles.csv',',')
data1 = data1.astype({'county': 'int64'})

#print(data1)
# select data syntax data1.loc[data1['county'] == 36061]
countyCode = 36061
countyTPop = (data1.loc[data1['county'] == countyCode])['population'].values[0]
countyDist = data2.loc[data2['county1'] == countyCode]
countyCodeAr = np.array(data1['county'])
countyPopAr = np.array(data1['population'])
noCounties = len(countyCodeAr)
moveAr = []
for i in range(noCounties):
    if countyCodeAr[i] != countyCode:
        dist = countyDist.loc[countyDist['county2'] == countyCodeAr[i]]['mi_to_county'].values[0]
        moveAr.append(migFlow(countyTPop,countyPopAr[i],dist))
    else:
        moveAr.append(0)
    
moveAr = np.array(moveAr)
dfTest = pd.DataFrame()
dfTest['fips'] = countyCodeAr
dfTest['unemp'] = moveAr
print(dfTest)
#print(len(moveAr))
#print(len(countyCodeAr))