import pandas as pd

pathFile = "/media/marcin/win_ssd/Users/m1/Desktop/jupyterNotebook/data.txt" # import os for path

"""for test
pathFile = "/media/marcin/win_ssd/Users/m1/Desktop/jupyterNotebook/ratings.csv"
dta = pd.read_csv(pathFile,dtype={"userId":'str','ItemId':'str'})
dta = dta.rename(columns={'userId':'idCus', 'ItemId':'sku'})
print(dta)
"""


dta = pd.read_csv(pathFile, sep=';', low_memory=False, dtype={"idCus":'str'})
dta = dta.loc[:,['idCus', 'sku', 'date']]
dta['date'] = pd.to_datetime(dta.date)
dta['month'] = dta['date'].dt.month
dta = dta.loc[dta.month == 1, ['idCus', 'sku']]

frameDta = dta.loc[:, ['idCus', 'sku']].drop_duplicates()
allSkuList = frameDta["sku"].unique().tolist() # upperCASE
all_userCount = len(frameDta["idCus"].unique().tolist())
mainFrame = pd.DataFrame(columns=('sku1', 'sku2', 'users', 'score'))

row = 0

skuList = ['DHSGTASDC07'] # input list skus
list1 = list()
list2 = list()
for sku1 in skuList:
    list1.append(sku1)
    sku1users = frameDta.loc[frameDta.sku == sku1, "idCus"].tolist()

    for sku2 in allSkuList:
        if sku1 != sku2:
            list2.append(sku2)
            sku2users = frameDta.loc[frameDta.sku == sku2, "idCus"].tolist()

            commonUsers = len(set(sku1users).intersection(set(sku2users)))
            score = commonUsers / all_userCount

            mainFrame.loc[row] = [sku1, sku2, commonUsers, score]
            row += 1
            mainFrame.loc[row] = [sku2, sku1, commonUsers, score]
            row += 1

            if len(list2) % 20 == 0:
                print("All_user: ", all_userCount, "SKU1: ", len(list1), "/", len(skuList), "SKU2: ", len(list2), "/", len(allSkuList))
            else:
                continue

#print(mainFrame.head())
checkItem = 'DHSGTASDC07'
recoList = mainFrame[mainFrame.sku1 == checkItem][["sku1", "sku2", 'users', "score"]].sort_values("score", ascending=False)

print('Recommendations', recoList)
