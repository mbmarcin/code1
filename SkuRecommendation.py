
import os
import pprint
print(os.environ['PATH'])
pprint.pprint(os.environ['PATH'].split(';'))




import pandas as pd
import numpy as np

data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
df = pd.DataFrame.from_dict(data)
print(df)

