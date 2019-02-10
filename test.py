# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 19:45:55 2019

@author: m1

def func():
    colors = ["red", "green", "blue", "purple"]
    i = 0
    a = list()
    for i in colors:
        a.append(i)
        xc = len(a)
        x = len(colors)
        if x != xc:
            print(x,xc)
        else:
            print("end")
    
func()
"""

import pandas as pd

path = 'C://Users//m1//Desktop//jupyterNotebook//data.txt'

"""
data from file---------------------------------------------------------------------------------------
"""

def getData(pathFile):
    data = pd.read_csv(pathFile, sep=';', low_memory=False, dtype={"idCus":'str'})
    return data

"""
data set after processing
"""

def data(data):
    dataSet = data.loc[:,['idCus','sku','date']].drop_duplicates()
    return dataSet

print(data(getData(path)))    