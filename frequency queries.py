# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 02:01:41 2018

@author: Zhang Wu
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    a={}    #store frequency
    b=[]    # store results of query 3
    c={i:0 for i in range(1,int(len(queries)/2)+1)} # store the number of apperance of given frequency
    for i in queries:
        if i[0]==1:
            if a.get(i[1]) == None:
                a[i[1]]=1
                c[1] += 1
            else: 
                c[a[i[1]]] -= 1
                a[i[1]]=a[i[1]]+1
                c[a[i[1]]] += 1
        elif i[0]==2:
            if a.get(i[1]) == None:
                continue
            elif a[i[1]]==1:
                c[1] -= 1
                del a[i[1]]
            else:
                c[a[i[1]]] -= 1
                a[i[1]]=a[i[1]]-1
                c[a[i[1]]] += 1
        else:
            if c[i[1]] != 0:
                b.append(1)
            else:
                b.append(0)
    return b