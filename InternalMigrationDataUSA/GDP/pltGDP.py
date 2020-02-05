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


data = pd.read_csv('countyGDP_v2.csv',',',dtype = {'fips': 'str'})
print(data.dtypes)
dfTest = pd.DataFrame()
dfTest['fips'] = data['fips']
dfTest['GDP'] = data['2015']



with open('../../../Data/geojson-counties-fips.json') as json_file:
    counties = json.load(json_file)

print(dfTest)
fig = px.choropleth_mapbox(dfTest, geojson=counties, locations='fips', color='GDP',
                           color_continuous_scale="Viridis",
                           mapbox_style="carto-positron",range_color=(0, 5000000),
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
