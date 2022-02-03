class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        n = len(s)//(2*k)
        flag = min(k,len(s)-2*k*n)
        for i in range(n):
            begin = 2*k*i
            end = 2*k*i+k-1
            while begin < end:
                s[begin], s[end] = s[end], s[begin]
                begin += 1
                end -= 1
        if 2*k*n < len(s):
            begin = 2*k*n
            end = 2*k*n+flag-1
            while begin < end:
                s[begin], s[end] = s[end], s[begin]
                begin += 1
                end -= 1
                
        return "".join(s)


##Another way
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)
