class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None:
            return 0
        curr = 0
        maxlen = 0
        mystack = []
        currlen = 0
        while curr < len(s):
            if s[curr] in mystack:
                index=mystack.index(s[curr])
                mystack.append(s[curr])
                mystack=mystack[index+1:len(mystack)]
                currlen = len(mystack)
                curr += 1
            else:
                mystack.append(s[curr])
                currlen += 1
                maxlen = max(maxlen, currlen)
                curr += 1 
        
        return maxlen
      
##O(2*n) = O(n)
##Another cleaner version
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None:
            return 0
        chars = [0] * 128
        left = right = 0
        res = 0
        
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1
                
            res = max(res, right - left + 1)
            right += 1
            
        return res
##optimize from 2n to n
class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        i = 0
        ans = 0 
        mp = {}
        
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            
            mp[s[j]] = j + 1
            ans = max(ans, j - i +1)
        
        return ans
