# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 13:45:08 2020

@author: lucas
"""

from urllib.request import urlopen
import json
import plotly.express as px
import pandas as pd
import numpy as np


data2 = pd.read_csv('../../../Data/countyPop2014_v3.csv',',',dtype = {'county': 'str'})

# select data syntax data1.loc[data1['county'] == 36061]
dfTest = pd.DataFrame()
dfTest['fips'] = data2['county']
dfTest['Population'] = data2['population']


with open('../../../Data/geojson-counties-fips.json') as json_file:
    counties = json.load(json_file)

cNo = len(counties["features"])
test = np.ones((cNo))
#print(df)
fig = px.choropleth_mapbox(dfTest, geojson=counties, locations='fips', color='Population',
                           color_continuous_scale="Viridis",
                           mapbox_style="carto-positron",range_color=(0, 1000000),
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()