#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    sequence = ['{','}','(',')','[',']']
    
    def match(a,b):
        if sequence.index(a) % 2 !=0:
            return False
        else:
            if sequence.index(b) == sequence.index(a)+1:
                return True
            else:
                return False
    stack = []
    i=0
    while i < len(s):
        if not stack:
            stack.append(s[i])
        elif match(stack[-1],s[i]):
            stack.pop()
        else:
            stack.append(s[i])
        i += 1
    if len(stack)>0:
        return("NO")
    else:
        return("YES")
           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()



###Another way without using stack
def isBalanced(s):
    # Write your code here
    n = -1
    while len(s) != n:
        n = len(s)
        s = s.replace('()','')
        s = s.replace('[]','')
        s = s.replace('{}','')
        
    if len(s)>0:
        return("NO")
    else:
        return("YES")
           
