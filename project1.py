# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 17:28:52 2019

@author: m1
"""

import pandas as pd


def getData(pathFile):
    data = pd.read_csv(pathFile, sep=';', low_memory=False, dtype={"idCus":'str'})
    return data


print(getData('C://Users//m1//Desktop//jupyterNotebook//data.txt').head())

