# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 17:28:52 2019

@author: m1
"""

import pandas as pd

path = 'C://Users//m1//Desktop//jupyterNotebook//data.txt'

def getData(pathFile):
    data = pd.read_csv(pathFile, sep=';', low_memory=False, dtype={"idCus":'str'})
    return data


"""
Top users per trader
"""
def top2PerTrader(data):
    sum_ = data.groupby(['idTr','idCus'],as_index=False)[['salesValue']].sum()
    han = data.loc[:,'idTr'].drop_duplicates()
    tr = []
    for i in [x.lower() for x in han]:
        perUser = sum_[sum_.idTr == i].sort_values(by=['salesValue'],ascending=False)[:2]
        idk = perUser.loc[:,'idCus'].tolist()
        if len(idk) == 2:
            tr.append(idk)     
    return tr

output = []
# function used for removing nested  lists in python. 
def removeNestings(list_): 
    for i in list_: 
        if type(i) == list: 
            removeNestings(i) 
        else: 
            output.append(i)
            
removeNestings(top2PerTrader(getData(path)))
print(output)

