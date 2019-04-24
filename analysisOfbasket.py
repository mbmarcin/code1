# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 11:57:07 2019

@author: aspr323
"""
from statistics import mean
import pandas as pd
from datetime import datetime

d_t = datetime.now().strftime('%d_%m_%Y_%H_%M') 
file = "data.txt"

def getData(nameFile):
    """idCus	team	year	month	Sales"""
    dataSet = pd.read_csv(nameFile, sep=';', low_memory=False, dtype={"idCus":'str'})
    return dataSet


def divisionIntoBaskets(dataSet):
    bins = [0,20,40,60,80,101]
    labels = [2,24,46,68,81]
    l1 = list()
    l2 = list()
    for year in dataSet.year.drop_duplicates(): # data for year
        t1 = dataSet.loc[(dataSet.year == year) & (dataSet.Sales > 0),['team','idCus','Sales','month']] # ZWRÓCIĆ UWAGĘ na klientów z minusowym obrotem
        print("Podział obortu na koszyki, rok: {0}" .format(year))
        for team in t1.team.drop_duplicates(): # data for team
            print("Podział obortu na koszyki, team: {0}".format(team))
            t2 = t1.loc[t1.team == team,['idCus','Sales','month']]
            for month in t2.month.drop_duplicates(): # data for month
                #print("Podział obortu na koszyki, miesiąc: {0}".format(month))
                t3 = t2.loc[t2.month == month,['idCus','Sales']]
                sumMonth = t3.Sales.sum()
                t3['share'] = (t3.Sales/sumMonth)*100
                t3 = t3.loc[:,['idCus','share']].sort_values(by = ['share'], ascending=False)
                t3['CumSum'] = t3.share.cumsum()
                t3['basket'] = pd.cut(t3['CumSum'], bins=bins, labels=labels).astype(int)

                #analysis of basket per customer
                t4 = t3.loc[:,['idCus','basket']]
                t4['month'] = month
                t4['year'] = year
                t4['team'] = team
                l1.append(t4)

                #analysis of basket
                t5 = t3.groupby(['basket'],as_index=False)[['idCus']].count()  #quantity of the customer in basket
                t5['month'] = month
                t5['year'] = year
                t5['team'] = team
                l2.append(t5)

    df1 = pd.concat(l1)#analysis of basket per customer
    df2 = pd.concat(l2)#analysis of basket year/month/team
    return df1, df2

def checkList(list_):
    list_.sort()
    if len(list_)-1 == 0: 
        return False
    else:
        i = 0
        while i < len(list_)-1:
            if list_[i+1]-list_[i] == 1:
                i+=1
            else:
                return False
    return True

def activityOFcustomer(dataSet):
    """
    activityMC,idCus,maxMC,minMC,regularity,year
    """
    mainList = list()
    for year in dataSet.year.drop_duplicates().sort_values(ascending=False): # list for years
        t1 = dataSet.loc[dataSet.year == year] # data for years
        print("Sprawdzanie aktywnosci klienta, rok: {0}" .format(year))
        for team in t1.team.drop_duplicates(): # list for teams
            t2 = t1.loc[t1.team == team] # data for team
            print("Sprawdzanie aktywnosci klienta, team: {0}" .format(year))
            for cus in t2.idCus.drop_duplicates(): # list for customer
                t3 = t2.loc[t2.idCus == cus,] # data for customer
                mcList = t3.month.drop_duplicates().sort_values().tolist()
                if len(mcList) == 12:
                    d1 = {'idCus':cus,
                          'regularity':'yes',
                          'activity':12, 
                          'min':1,
                          'max':12, 
                          'year':t3.year.max()} 
                    mainList.append(d1)
                elif checkList(mcList) == True:
                    d2 = {'idCus':cus,
                          'regularity':'yes',
                          'activity':len(mcList),
                          'min':min(mcList),
                          'max':max(mcList),
                          'year':t3.year.max()}
                    mainList.append(d2)
                else:
                    d3 = {'idCus':cus,
                          'regularity':'no',
                          'activity':len(mcList),
                          'min':min(mcList),
                          'max':max(mcList),
                          'year':t3.year.max()
                         }
                    mainList.append(d3)  
    return pd.DataFrame(mainList)
#regularityOFcustomer(data).head()#.to_csv('regularityOFcustomer.txt',sep=',')   
#print(activityOFcustomer(getData(file)).head())

def best_fit_slope(xs,ys):
    """
    machine learning regression
    https://pythonprogramming.net/how-to-program-best-fit-line-machine-learning-tutorial/
    """
    m = (((mean(xs)*mean(ys)) - mean(xs*ys))/((mean(xs)*mean(xs)) - mean(xs*xs)))
    #b = mean(ys) - m*mean(xs)
    return m #,b

def slopeOfbaskets(dataFrame):
    lSlope = list()
    
    for cus in dataFrame.idCus.drop_duplicates():
        tSlope = dataFrame.loc[dataFrame.idCus == cus].sort_values(by='month')
        year = tSlope.year.drop_duplicates().tolist()
        mode = ','.join(map(str, tSlope.basket.mode().tolist()))#tSlope.basket.mode().tolist()
        lastMonthBasket = tSlope.loc[tSlope.month == tSlope.month.max()].basket.max()
        firstMonthBasket = tSlope.loc[tSlope.month == tSlope.month.min()].basket.min()
        try:
            m = round(best_fit_slope(tSlope.month,tSlope.basket),4)
            d1 = {
                'idCus':cus,
                'year':year[0],
                'slopeBaskets':m,
                'mode':mode,
                'lastMonthBasket':lastMonthBasket,
                'firstMonthBasket':firstMonthBasket
            }
            lSlope.append(d1) 
        except ZeroDivisionError:
            d2 = {
                'idCus':cus,
                'year':year[0],
                'slopeBaskets':None,
                'mode':mode,
                'lastMonthBasket':lastMonthBasket,
                'firstMonthBasket':firstMonthBasket
            }
            lSlope.append(d2) 
    return pd.DataFrame(lSlope)

a, b = divisionIntoBaskets(getData(file))
b.to_csv('QuantityCustomerBasket_{0}.txt'.format(d_t),sep=';',index=False, header=True) # save file

def main():
    """
    main dataFrame
    """
    t1 = a
    t_avg = t1.groupby(['idCus','year','team'],as_index=False).agg({'basket' : ['min', 'max', 'mean']})
    t_avg.columns = [''.join(col) for col in t_avg.columns] 
    main = pd.merge(activityOFcustomer(getData(file)),slopeOfbaskets(t1),on=['idCus','year']).merge(t_avg, on=['idCus','year'])
    return main.to_csv('tableOFbasket_{0}.txt'.format(d_t),sep=';',index=False, header=True)# save file

main()
print("Plik QuantityCustomerBasket zapisany")
print("Plik tableOFbasket zapisany")
    


    



