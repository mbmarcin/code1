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
    dataSet.loc[:,'date'] = pd.to_datetime(dataSet.date)
    return dataSet


def top2PerTrader(data):
    """
    Top users per trader
    """
    sum_ = data.groupby(['idTr','idCus'],as_index=False)[['salesValue']].sum()
    data.loc[:,'idTr'] = [x.lower() for x in data.loc[:,'idTr']]
    han = data.loc[:,'idTr'].drop_duplicates()
    tr = []
    for i in han:
        perUser = sum_[sum_.idTr == i].sort_values(by=['salesValue'],ascending=False)[:2]
        idk = perUser.loc[:,'idCus']
        if len(idk) == 2:
            tr.append(idk) 
    tr_ = [j for i in tr for j in i] # remove nested list
    dic = {
        'idCus':tr_
    }
    df1 = pd.DataFrame(dic).drop_duplicates()
    mainList = df1.loc[:,'idCus'].tolist()
    return mainList                 

#df.to_csv("idList.txt")  #print(df) 
#print(top2PerTrader(getData(path)))


def checkQuarter(data):
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
        dataSET = data[data.idCus == i]
        idProduct = dataSET.loc[:,'sku'].drop_duplicates().tolist() #product list 
        counter2 = list()     
        for i in idProduct:
            counter2.append(i)
            counter_2 = len(counter2)
            all_2 = len(idProduct)
            print("{0} sku/".format(counter_2),"{0}".format(all_2))
            print("{0} customer/".format(counter_1),"{0}".format(all_1))
            t2 = dataSET[dataSET.sku == i]
            #t2.loc[:,'date'] = pd.to_datetime(t2.date)
            q = t2.loc[:,'date'].dt.quarter.drop_duplicates()
            if sum(q) == 10:
                idi = t2.loc[:,['idCus','sku']].drop_duplicates()
                listOK.append(idi)
            #else:
                #list2.append(idi)
    a = pd.concat(listOK)
    a.to_excel('listOK2.xlsx')
    return print("listOK saved")
checkQuarter(data())

"""
# regularity per prduct
customer = #customer list
maxMin = {'date':('2011-01-01','2011-12-31')}
frameMaxMin = pd.DataFrame(maxMin)
frameMaxMin.loc[:,'date'] = pd.to_datetime(frameMaxMin.date)
list_dict = list()

for i in customer:
    data = dataSet[dataSet.idCus == i] # Data set for loop
    idProduct = #data['sku'].tolist() #product list
    setdata = {
        'idCus':[i]*len(idProduct),
        'sku':[],
        'avg':[],
        'std':[]
    }
    for i in idProduct:
        t = data[data.sku == i]
        t = t.loc[:,'date'].to_frame().drop_duplicates()
        # concat with whole range date(max,min)
        t2 = pd.concat([frameMaxMin,t])
        #------------------------------------------------------------------
        t2 = t2.sort_values(by=['date'],ascending=True)
        t2.loc[:,'date_new'] = t2.loc[:,'date'].shift(periods=1, freq=None, axis=0)
        t2.loc[:,'df_date'] = (t2['date'] - t2['date_new']).dt.days
        avg = round(t2.loc[:,'df_date'].mean(),3)
        std = round(t2.loc[:,'df_date'].std(),3)
        setdata['sku'].append(i)
        setdata['avg'].append(avg)
        setdata['std'].append(std)
    #x = pd.DataFrame.from_dict(setdata)
    list_dict.append(setdata)

main = []
for i in range(0,len(list_dict)):
    x = pd.DataFrame(list_dict[i])
    main.append(x)
pd.concat(main)  
"""