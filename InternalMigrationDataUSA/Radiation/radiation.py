# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:04:17 2020

@author: lucas
"""

import json
import plotly.express as px
import pandas as pd
import numpy as np


def migFlow(popDest,sij):
    migFrac = .1
    popOrigin = 202000
    return((migFrac*popDest*popOrigin**2)/((popOrigin+sij)+(popOrigin+popDest+sij)))

data1 = pd.read_csv('../../../Data/sij_01125.csv',',',dtype = {'fips': 'str'})

popAr = data1['pop']
sijAr = data1['sij']


noCounties = len(popAr)
moveAr = []
for i in range(noCounties):
    move = migFlow(popAr[i],sijAr[i])
    moveAr.append(move)   
    print(i)

moveAr = np.array(moveAr)
dfTest = pd.DataFrame()
dfTest['fips'] = data1['fips']
dfTest['Migrants'] = moveAr

print(dfTest)

with open('../../../Data/geojson-counties-fips.json') as json_file:
    counties = json.load(json_file)
    
test = np.ones((len(counties["features"])))
fig = px.choropleth_mapbox(dfTest, geojson=counties, locations='fips', color='Migrants',
                           color_continuous_scale="Viridis",
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
