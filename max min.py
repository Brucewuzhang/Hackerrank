# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 02:06:12 2018

@author: Zhang Wu
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    m=arr[k-1]-arr[0]
    for i in range(k-1,len(arr)):
        if arr[i]-arr[i-k+1]<m:
            m=arr[i]-arr[i-k+1]
    return m