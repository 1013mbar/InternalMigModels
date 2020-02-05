#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:47:23 2020

@author: kluge
"""

import pandas as pd
import numpy as np

data = pd.read_csv("../../../Data/sf12010countydistancemiles.csv",',')
data2 = pd.read_csv("../../../Data/countyPop2014_v1.csv",';')
data2 = data2.dropna()
np.savetxt("../../../Data/countyPop2014_v2.csv",data2)
print(data2)