#!/bin/python3

import math
import os
import random
import re
import sys


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    graph = [[] for x in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    queue = []
    visited = [False] * (n+1)
    dist = [-1] * (n+1)
    dist[s] = 0
    visited[s] = True
    queue.append(s)
    while queue:
        s1 = queue.pop(0)
        for v in graph[s1]:
            if visited[v] == False:
                visited[v] = True
                dist[v] = dist[s1] + 6
                queue.append(v)
    dist.pop(s)
    dist.pop(0)
    return dist




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

###Below are my wrong codes...


# Complete the 'bfs' function below. 
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    # Write your code here
    mydict = {}
    output = [-1] * (n+1)
    for uv in edges:
        if uv[0] not in mydict:
            mydict[uv[0]]=[uv[1]]
        else:
            mydict[uv[0]].append(uv[1])
    queue = []
    for v in mydict[s]:
        queue.append([v,1])
    while queue:
        v,ed = queue.pop(0)
        if output[v] == -1:
            output[v] = ed*6
            if v in mydict:
                for v1 in mydict[v]:
                    queue.append([v1,ed+1])
    output.pop(s)
    output.pop(0)
    return output
if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
