class Solution:
    def isPalindrome(self, s: str) -> bool:
        s
        l = 0
        r = len(s)-1 
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
               
            else:
                l += 0 if s[l].isalnum() else 1
                r -= 0 if s[r].isalnum() else 1
                
        return True
        
