class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower().replace(" ", "")
        l = 0
        r = len(s1)-1 
        while l < r:
            if s1[l].isalnum() and s1[r].isalnum():
                if s1[l] != s1[r]:
                    return False
                else:
                    l += 1
                    r -= 1
               
            else:
                l += 0 if s1[l].isalnum() else 1
                r -= 0 if s1[r].isalnum() else 1
                
        return True
        
