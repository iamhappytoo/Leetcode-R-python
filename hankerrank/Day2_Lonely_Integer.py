#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    mydict = {}
    for num in a:
        mydict[num]=mydict.get(num,0)+1
    for num in mydict:
        if mydict[num]==1:
            return num
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
