# Enter your code here. Read input from STDIN. Print output to STDOUT
olds = []
s = ""
Q = int(input())
for _ in range(Q):
    val = input().split()
    if int(val[0]) == 1:
        olds.append(s)
        s = s + val[1]        
    elif int(val[0]) == 2:
        olds.append(s)
        k = int(val[1])
        s = s[0:(len(s)-k)]
    elif int(val[0]) == 3:
        k = int(val[1])
        print(s[k-1])
    else:
        s = olds.pop()
