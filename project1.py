# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 17:28:52 2019

@author: m1
"""

import pandas as pd

path = 'C://Users//m1//Desktop//jupyterNotebook//data.txt'

def getData(pathFile):
    """
    data from file
    """
    data = pd.read_csv(pathFile, sep=';', low_memory=False, dtype={"idCus":'str'})
    return data

def data():
    """
    data set after processing
    """
    data = getData(path)
    dataSet = data.loc[:,['idCus','sku','date']].drop_duplicates()
    return dataSet

def top2PerTrader(data):
    """
    Top users per trader
    """
    sum_ = data.groupby(['idTr','idCus'],as_index=False)[['salesValue']].sum()
    han = data.loc[:,'idTr'].drop_duplicates()
    tr = []
    for i in [x.lower() for x in han]:
        perUser = sum_[sum_.idTr == i].sort_values(by=['salesValue'],ascending=False)[:2]
        idk = perUser.loc[:,'idCus'].tolist()
        if len(idk) == 2:
            tr.append(idk) 
    tr_ = [j for i in tr for j in i]
    #trList = {'idCus':[j for i in tr for j in i]}
    #df = pd.DataFrame(trList)
    return tr_                  #df.to_csv("idList.txt")  #print(df) 

#print(top2PerTrader(getData(path)))


def checkQuarter(dataSet):
    """
    Check quarter per product
    """
    customer = top2PerTrader(getData(path))#customer list
    listOK = []
    counter1 = list()
    for i in customer:
        counter1.append(i)
        counter_1 = len(counter1)
        all_1 = len(customer)        
        data = dataSet[dataSet.idCus == i]
        idProduct = data.loc[:,'sku'].tolist() #product list 
        counter2 = list()
        for i in idProduct:
            counter2.append(i)
            counter_2 = len(counter2)
            all_2 = len(idProduct)
            print(counter_2,all_2)
            print(counter_1,all_1)
            t2 = data[data.sku == i]
            t2.loc[:,'date'] = pd.to_datetime(t2.date)
            q = t2.loc[:,'date'].dt.quarter.drop_duplicates()
            if sum(q) == 10:
                idi = t2.loc[:,['idCus','sku']].drop_duplicates()
                listOK.append(idi)
            #else:
                #list2.append(idi)
    a = pd.concat(listOK)
    #b = pd.concat(list2)
    a.to_excel('listOK.xlsx')
    #b.to_excel('list2.xlsx')
    return print("list_saved")
checkQuarter(data())