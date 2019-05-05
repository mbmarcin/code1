import os
import glob
from pathlib import Path
"""
file = 'data.txt'
os.chdir("~/media/marcin/")
print(os.path.abspath(file))


for r,s,f in os.walk("."):
    for i in f:
        if file in i:
            print(os.path.join(r,i))
"""

#for file in glob.glob('/media/*.csv')

print(
    sorted(Path('.').glob('*.py'))
)