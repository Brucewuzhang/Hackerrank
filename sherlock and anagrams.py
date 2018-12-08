# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 01:56:54 2018

@author: Zhang Wu
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count =0
    for i in range(1,len(s)):
        b={}
        for j in range(len(s)-i+1):
            c=list(s[j:j+i])
            c.sort()
            c=''.join(c)
            b[c]=b.get(c,0)+1
        for k,v in b.items():
            count += v*(v-1)/2
    return int(count)