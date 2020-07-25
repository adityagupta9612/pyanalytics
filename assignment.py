#denco assignment

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 01:39:58 2020

@author: aditya
"""

import pandas as pd
import numpy as np

data=pd.read_csv('denco.csv')
data.head()
data.columns
data.dtypes

arr=data['custname']
a=arr.value_counts()
print(a[0])


dir(arr)
data.groupby('custname').size().max()
data.groupby('custname').size().plot(kind='bar')
dir(data)
set(data)
data['custname'].max()

#most loyal customer
grouped_single=data.custname.value_counts('')
grouped_single
grouped_single.sort_values(ascending=False).head(5)

#most contribution to revenue
grouped_single=data.groupby(['custname','region']).agg({'revenue':sum,'margin':'mean'})
grouped_single.sort_values('revenue',ascending=False)


