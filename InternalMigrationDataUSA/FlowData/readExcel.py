# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:26:47 2020

@author: lucas
"""

import pandas as pd
import numpy as np

data = pd.read_csv('Alabama.csv',';',dtype = str)
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
	

#data['fipsA'] = data['fipsA'].astype(int)
data.to_csv('testProc.csv')
