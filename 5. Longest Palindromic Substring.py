class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findmaxpalin(s, curr):
            tempstack = [s[curr]]
            if curr == 0:
                while curr < len(s)-1 and s[curr+1]==s[curr]:
                    tempstack.append(s[curr+1])
                    curr += 1
                return tempstack
            elif curr == len(s)-1:
                while curr > 0 and s[curr-1] == s[curr]:
                    tempstack.append(s[curr-1])
                    curr -= 1
                return tempstack
            else:
                left = curr
                right = curr
                while right < len(s) and s[right] == s[curr]:
                    right += 1
                while left >= 0 and s[left] == s[curr]:
                    left -= 1
                while left >=0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
                
                tempstack = s[left+1:right]
                return tempstack
        if len(s) <= 1:
            return s
        curr = 0
        left=0
        right = 0
        maxlen = 0
        stack = []
        while curr < len(s):
            tempstack = findmaxpalin(s, curr)
            if len(tempstack) > maxlen:
                stack = tempstack
                maxlen = len(tempstack)
            curr += 1
        return ''.join(stack)
            
        
        
                    
            
