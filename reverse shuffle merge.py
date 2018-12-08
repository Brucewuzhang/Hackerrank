# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 02:04:21 2018

@author: Zhang Wu
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    a=[]
    b={}
    d={}
    c=''
    for i in range(len(s)):
        a.append(s[len(s)-1-i])
        b[s[i]]=b.get(s[i],0)+1
    for k,v in b.items():
        b[k]=int(v/2)
    d=b.copy()
    start=0
    l=len(a)
    while start != l-1:
        for i in range(start,l):
            if len(c) == int(l/2):
                return c
            if b[a[i]] !=0:
                b[a[i]]=b[a[i]]-1
            elif start != i:
                m='{'
                t=start
                for j in range(start,i):
                    if d[a[j]]!=0 and a[j]<m:
                        m=a[j]
                        t=j
                c +=m
                for j in range(t,i):
                    b[a[j]] +=1
                d[m] = d[m] - 1
                start=t+1
                break
            else:
                c += a[i]
                d[a[i]] -= 1
                start += 1
    if d[a[l-1]]!=0:
        c += a[l-1]
    return c