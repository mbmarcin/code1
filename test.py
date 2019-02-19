# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 19:45:55 2019

@author: m1

def func():
    colors = ["red", "green", "blue", "purple"]
    i = 0
    a = list()
    for i in colors:
        a.append(i)
        xc = len(a)
        x = len(colors)
        if x != xc:
            print(x,xc)
        else:
            print("end")
    
func()
"""


import os, glob

def pathFile(FileName):
    """
    return path file from current dir
    """
    cat = os.getcwd()
    path = os.path.join(cat,FileName)
    return glob.glob(path)

print(pathFile("listOK.txt"))




#print(os.chdir("/m1/Desktop/jupyterNotebook"))


