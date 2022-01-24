#!/bin/python3

import math
import os
import random
import re
import sys

# m = 4: [4, 13, 22, 112, 1111]
# m = 3: [111, 12, 3] 
# 1. every possible ways m=5: [11111, 1112 * 4, 113 * 3, 14 * 1, ]
# 1+(ways)
# 2+(ways)
# 3+(ways)
# 4+(ways)
# 2. n = 2: 4^n = 4^2 = 16
# 3. remove not possible cases: (111, 12) permutations, (21), (111), (12)
# that is: 2^2 + 1 + 1 + 1=7 
# 4. 16 - 7 = 9
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
mydict={}
def getwaysnum(m):
    if m == 0:
        return 1
    if m < 0:
        return 0
    if m-1 not in mydict:
        mydict[m-1] = getwaysnum(m-1)
    if m-2 not in mydict:
        mydict[m-2] = getwaysnum(m-2)
    if m-3 not in mydict:
        mydict[m-3] = getwaysnum(m-3)
    if m-4 not in mydict:
        mydict[m-4] = getwaysnum(m-4)    
    return(mydict[m-1]+mydict[m-2]+mydict[m-3]+mydict[m-4])
        
    #return(getwaysnum(m-1)+getwaysnum(m-2)+getwaysnum(m-3)+getwaysnum(m-4))
def legoBlocks(n, m):
    # Write your code here    
    numways = getwaysnum(m) 
    allways = numways ** n
    Sumnoway = 0
    for i in range(1,m):
        Sumnoway += legoBlocks(n,i) * mydict[m-i]**n
    return (allways - Sumnoway) % (1000000007)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
####Above codes are too slow, here is iterative solution which is much faster (time complexity is o(m2))
#!/bin/python3

import math
import os
import random
import re
import sys

# m = 4: [4, 13, 22, 112, 1111]
# m = 3: [111, 12, 3] 
# 1. every possible ways m=5: [11111, 1112 * 4, 113 * 3, 14 * 1, ]
# 1+(ways)
# 2+(ways)
# 3+(ways)
# 4+(ways)
# 2. n = 2: 4^n = 4^2 = 16
# 3. remove not possible cases: (111, 12) permutations, (21), (111), (12)
# that is: 2^2 + 1 + 1 + 1=7 
# 4. 16 - 7 = 9
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


mydictlb = {}
def legoBlocks(n, m):
    mydict={}
    A = 1000000000 + 7
    a = [0] * (m+1)
    r = [0] * (m+1)
    a[0] = 1
    for j in range(1,m+1):
        a[j] += a[j-1] if j-1 >=0 else 0
        a[j] += a[j-2] if j-2 >=0 else 0
        a[j] += a[j-3] if j-3 >=0 else 0
        a[j] += a[j-4] if j-4 >=0 else 0
    # Write your code here    
    for j in range(1,m+1):
        a[j] = a[j] % A
        a[j] = a[j] ** n 
        a[j] = a[j] % A
    r[1] = 1
    for j in range(2, m+1):
        r[j] = a[j]
        for k in range(1,j):
            r[j]-= r[k]*a[j-k]
        r[j] = r[j] % A
    return r[m]%A
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
