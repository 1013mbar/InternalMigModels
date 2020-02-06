# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:26:47 2020

@author: lucas
"""

import pandas as pd
import numpy as np

data = pd.read_csv('../../../Data/California.csv',';',dtype = str)
#data1 = np.genfromtxt('Alabama.csv')
#data.drop(['Unnamed: 12','Unnamed: 13','Unnamed: 14','Unnamed: 15'],axis = 1)
data = data.astype(str)

data = data.dropna(axis= 0,how = 'any')
data = data[data['County Name of Geography B'] != '-']
data['fipsA'] = data['State Code of Geography A']+data['FIPS County Code of Geography A']
data['fipsB'] = data['State/U.S. Island Area/Foreign Region Code of Geography B']+data['FIPS County Code of Geography B']
data = data.drop(['State Code of Geography A','FIPS County Code of Geography A',
                  'State/U.S. Island Area/Foreign Region Code of Geography B',
                  'FIPS County Code of Geography B','State Name of Geography A',
                  'County Name of Geography A',
                  'State/U.S. Island Area/Foreign Region of Geography B',
                  'County Name of Geography B'],axis=1)
	

data = data.dropna(axis=1,how='any')
newDF = pd.DataFrame()

fipsA = np.array(data['fipsA'])
fipsB = np.array(data['fipsB'])
for i in range(len(fipsA)):
    if len(fipsA[i]) > 5:
        fipsA[i] = (fipsA[i])[1:]

for i in range(len(fipsB)):
    if len(fipsB[i]) > 5:
        fipsB[i] = (fipsB[i])[1:]
newDF['fipsA'] = fipsA
newDF['fipsB'] = fipsB
newDF['Flow from Geography B to Geography A'] = data['Flow from Geography B to Geography A']
newDF['flowBA'] = data['Counterflow from Geography A to Geography B1']
newDF['netAB'] = data['Net Migration from Geography B to Geography A1']
newDF['netBA'] = data['Gross Migration between Geography A and Geography B1']

newDF.to_csv('californiaFlowData.csv')
