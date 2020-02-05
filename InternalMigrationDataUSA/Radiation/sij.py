# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:36:57 2020

@author: lucas
"""

from urllib.request import urlopen
import json
import plotly.express as px
import pandas as pd
import numpy as np

data1 = pd.read_csv('../../../Data/sortedPop_01125.csv',',',dtype = {'fips': 'str'})
#data2 = pd.read_csv('sf12010countydistancemiles.csv',',',dtype = {'county1': 'str', 'county2': 'str'})
#countyCode = "01125"
popOrigin = 202000

pop = data1['population']
fips = data1['fips']
dist = data1['dist']

noCnt = len(fips)

sij = []

for i in range(noCnt):
    sijT = 0
    for j in range(i):
        sijT += dist[j]
    sij.append(sijT)
    print(i)


opp = pd.DataFrame()
opp['fips'] = fips
opp['sij'] = np.array(sij)
opp['pop'] = pop
opp['dist'] = dist
print(opp)

filename = 'sij_' + countyCode + '.csv'
opp.to_csv(filename)