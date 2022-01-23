#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    sarr = "abcdefghijklmnopqrstuvwxyz"
    sarr2 = sarr.upper()
    chout = ""
    for i,ch in enumerate(s):
        if ch in sarr:
            chout=chout+sarr[(sarr.find(ch)+k)%26]
        elif ch in sarr2:
            chout=chout+sarr2[(sarr2.find(ch)+k)%26]
        else:
            chout=chout+ch
    return(chout)
  
def caesarCipher(s, k):
    # Write your code here
    chout = ""
    for ch in s:
        if ch.islower():
            chout += chr((ord(ch)-97+k)%26+97)
        elif ch.isupper():
            chout += chr((ord(ch)-65+k)%26+65)
        else:
            chout += ch
    return(chout)
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
