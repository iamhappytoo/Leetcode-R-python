def pairs(k, arr):
 # Write your code here
 arr.sort()
 mydict = {}
 Sum = 0
 for num in arr:
 Sum += mydict.get(num-k,0)
 mydict[num] = mydict.get(num, 0) + 1
 return Sum
