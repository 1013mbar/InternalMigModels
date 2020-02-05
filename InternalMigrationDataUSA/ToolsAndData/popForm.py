# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:42:46 2020

@author: lucas
"""

import pandas as pd
import numpy as np

data1 = pd.read_csv('../../../Data/countyPop2014_v2.csv',' ')
data1 = data1.astype({'county': 'int64'})
data1 = data1.astype({'county': 'str'})
print(data1.iloc[2,0])
for i in range(len(data1)):
    if(len(data1.iloc[i,0]) < 5):
        data1.iloc[i,0] = str(0) + str(data1.iloc[i,0])
        print(data1.iloc[i,0])
data1.to_csv('../../../Data/countyPop2014_v3.csv',',')