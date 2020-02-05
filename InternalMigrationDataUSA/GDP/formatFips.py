# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:28:15 2020

@author: lucas
"""

import pandas as pd
import numpy as np

data = pd.read_csv('countyGDP_v1.csv',';',dtype = {'fips': 'str'})
fips  = data['fips']
gdp2015 = data['2015']
gdp2016 = data['2016']
gdp2017 = data['2017']
gdp2018 = data['2018']

for i in range(len(fips)):
    gdp2015[i] = gdp2015[i].replace('.','')
    gdp2016[i] = gdp2016[i].replace('.','')
    gdp2017[i] = gdp2017[i].replace('.','')
    gdp2018[i] = gdp2018[i].replace('.','')
    if len(fips[i]) == 4:
        fips[i] = '0'+fips[i]
data.to_csv('countyGDP_v2.csv')