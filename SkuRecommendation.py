
import pandas as pd

pathFile = "/media/marcin/win_ssd/Users/m1/Desktop/jupyterNotebook/data.txt" # import os for path

dta = pd.read_csv(pathFile, sep=';' ,low_memory=False, dtype={"idCus":'str'})
dta = dta.loc[:,['idCus','sku','date']]

frame = dta.loc[: ,['idCus' ,'sku']].drop_duplicates()
itemList = frame["sku"].unique().tolist() # upperCASE
all_userCount = len(frame["idCus"].unique().tolist())
mainFrame = pd.DataFrame(columns=('sku1' ,'sku2' ,'score'))

row = 0
for sku1 in range(len(itemList)):
    sku1ItemUser = frame[frame.sku == itemList[sku1]]["idCus"].tolist()

    for sku2 in range(sku1, len(itemList)):
        if sku1 == sku2:
            continue
        sku2ItemUser = frame[frame.sku == itemList[sku2]]["idCus"].tolist()

        commonUsers = len(set(sku1ItemUser).intersection(set(sku2ItemUser)))
        score = commonUsers / all_userCount

        mainFrame.loc[row] = [itemList[sku1], itemList[sku2], score]
        row += 1
        mainFrame.loc[row] = [itemList[sku2], itemList[sku1], score]
        row += 1

        print("All SKU: ", len(itemList),"SKU1: ", sku1, "SKU2: ",sku2, "all_userCount: ", all_userCount)


#checkItem = 'OOXXXSW7H6C'

print(mainFrame.head())
"""
recoList = mainFrame[mainFrame.sku1 == checkItem][["sku2", "score"]].sort_values("score", ascending=False)
print("Recommendations", recoList.head(20))
"""