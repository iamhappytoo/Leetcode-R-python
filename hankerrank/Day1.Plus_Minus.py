#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    posnum = 0
    negnum = 0
    zeronum = 0
    for i in arr:
        if i > 0:
            posnum += 1
        elif i ==0:
            zeronum += 1
        else:
            negnum +=1
    print(round((posnum/len(arr)),6))
    print(round((negnum/len(arr)),6))
    print(round((zeronum/len(arr)),6))    
    
n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
