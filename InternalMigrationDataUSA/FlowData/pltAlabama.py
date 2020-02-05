# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:00:17 2020

@author: lucas
"""

from urllib.request import urlopen
import json
import plotly.express as px
import pandas as pd
import numpy as np


data1 = pd.read_csv('../../../Data/alabamaFlowData.csv',',',dtype = {'fipsA': 'str', 'fipsB': 'str'})
data2 = pd.read_csv('../../../Data/countyPop2014_v3.csv',',',dtype = {'county': 'str'})

# select data syntax data1.loc[data1['county'] == 36061]
countyCode = "01073"
countyFlow = (data1.iloc[np.where(data1.fipsA.values == countyCode)])

dfTest = pd.DataFrame()
dfTest['fips'] = countyFlow['fipsB']
dfTest['Migrants'] = countyFlow['Flow from Geography B to Geography A']

noCnt = len(data2['county'])
Cnts = np.array(data2['county'])
CntsData = np.array(dfTest['fips'])
newCnts = []
for i in range(len(Cnts)):
    if not(np.any(CntsData == Cnts[i])):
        newCnts.append(Cnts[i])

dfExtend = pd.DataFrame()
dfExtend['fips'] = newCnts
dfExtend['Migrants'] = np.zeros(len(newCnts))

dfTest = dfTest.append(dfExtend)


with open('../../../Data/geojson-counties-fips.json') as json_file:
    counties = json.load(json_file)

cNo = len(counties["features"])
test = np.ones((cNo))
#print(df)
fig = px.choropleth_mapbox(dfTest, geojson=counties, locations='fips', color='Migrants',
                           color_continuous_scale="Viridis",
                           mapbox_style="carto-positron",range_color=(0, 52),
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
