class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or not needle:
            return -1 
        lenNeedle = len(needle)

        if lenNeedle == 0 or lenNeedle > len(haystack):
            return -1
        
        for i in range(len(haystack) - lenNeedle + 1):
            flag = 0
            for m in range(i,i + lenNeedle):
                if flag == 0 and haystack[m] == needle[m - i]:
                    continue
                else:
                    flag = 1
            if flag == 0:
                return i
        return -1     
      
      
##Use hashcode to change the time complexity to O(m+n):
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or not needle:
            return -1 
        m = len(needle)
        if m == 0 or m > len(haystack):
            return -1
        hashtarget = hash(needle)
        for i in range(len(haystack) - m + 1):
            if hash(haystack[i:(i + m)]) != hashtarget:
                continue
            else:
                if haystack[i:(i + m)] == needle:
                    return i
        return -1 
