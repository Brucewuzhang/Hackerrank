# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 22:37:24 2018

@author: Zhang Wu
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    a={}  # store frequency of single number before iteraration position
    b={}  # store frequence of lenth two gemetrci sequence before iteraration position
    count=0
    l=len(arr)
    for i in range(l):
        j=int(arr[i]/r)
        if j== arr[i]/r:

            count += b.get(j,0)
            b[arr[i]]=a.get(j,0)+b.get(arr[i],0)
        a[arr[i]]=a.get(arr[i],0)+1

    return count