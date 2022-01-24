#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

###The code below is too slow.
def noPrefix(words):
    # Write your code here
    mysave = []
    for i in range(len(words)-1):
        for j in range(i+1,len(words)):
            if words[j].startswith(words[i]) or words[i].startswith(words[j]):
                mysave.append(j)
    if len(mysave)==0:
        print("GOOD SET")
    else:
        print("BAD SET")
        print(words[min(mysave)])
        
if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
###There is the improved version:
