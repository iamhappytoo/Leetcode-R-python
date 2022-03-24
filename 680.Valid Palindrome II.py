class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        left = 0
        right = len(s)-1 
        flag = 0
        while left < right:
            if s[left] != s[right]:
                return check_palindrome(s, left, right-1) or check_palindrome(s, left+1, right)
            left += 1
            right -= 1
                
        return True
      
            
