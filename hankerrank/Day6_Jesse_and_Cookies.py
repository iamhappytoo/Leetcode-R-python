#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#
'''
# Write your code here
    step = 0
    while min(A) < k and len(A)>=2:
        A.sort()
        val = A[0:2]
        new = val[0]+val[1]*2
        A.pop(0)
        A.pop(0)
        A.append(new)
        step += 1
    if min(A) < k:
        return -1
    else:
        return step
    '''
def cookies(k, A):
    heapq.heapify(A)
    step = 0
    while A[0] < k and len(A)>=2:
        val1,val2 = heapq.heappop(A), heapq.heappop(A)
        heapq.heappush(A,val1+2*val2)
        step += 1
    if A[0] < k:
        return -1
    else:
        return step
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
