from urllib.request import urlopen
import json
import plotly.express as px
import pandas as pd
import numpy as np


def migFlow(pop1,pop2,distance):
    A = .00000007
    a = 1
    b = 1
    g = 1
    return(A*((pop1**a)*(pop2**b))/(distance**g))

data1 = pd.read_csv('../../../Data/countyPop2014_v3.csv',',',dtype = {'county': 'str'})
data2 = pd.read_csv('../../../Data/sf12010countydistancemiles.csv',',',dtype = {'county1': 'str', 'county2': 'str'})
countyCode = "01125"
countyTPop = (data1.iloc[np.where(data1.county.values==countyCode)])['population'].values[0]
countyDist = data2.loc[data2['county1'] == countyCode]
countyCodeAr = np.array(data1['county'])
countyPopAr = np.array(data1['population'])
noCounties = len(countyCodeAr)
moveAr = []
for i in range(noCounties):
    if countyCodeAr[i] != countyCode:
        dist = countyDist.iloc[np.where(countyDist.county2.values == countyCodeAr[i])]['mi_to_county'].values[0]
        moveAr.append(migFlow(countyTPop,countyPopAr[i],dist))
    else:
        moveAr.append(0)   
moveAr = np.array(moveAr)
dfTest = pd.DataFrame()
dfTest['fips'] = countyCodeAr
dfTest['Migrants'] = moveAr
print(countyCode)
dfTest.to_csv('fipsCodes.csv')

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
