

import pandas as pd

pathFile = "/media/marcin/win_ssd/Users/m1/Desktop/jupyterNotebook/data.txt"
#/media/marcin/dane_ssd/python/forLinux/ratings.csv
#/media/marcin/win_ssd/Users/m1/Desktop/jupyterNotebookdata.txt


dta = pd.read_csv(pathFile, sep=';',low_memory=False, dtype={"idCus":'str'})
frame = dta.loc[:,['idCus','sku']].drop_duplicates()
#usecols=['date','idCus']


print(frame.head())