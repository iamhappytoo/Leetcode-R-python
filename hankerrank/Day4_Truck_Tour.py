#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    for i, PD in enumerate(petrolpumps):
        if PD[0] < PD[1]:
            continue
        else:
            truck=PD[0]-PD[1]
            j = i+1
            while j != i:
                PDnew = petrolpumps[j]
                truck += PDnew[0]-PDnew[1]
                if truck >= 0:
                    j = (j+1) % len(petrolpumps)
                else:
                    break
            if j != i: 
                continue
            else:
                return i
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
