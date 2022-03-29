class Solution:
    def isPalindrome(self, x: int) -> bool:
        str1=str(x)
        pt1=0
        pt2=len(str1)-1
        while pt1<pt2:
            if str1[pt1] != str1[pt2]:
                return False
            else:
                pt1+=1
                pt2-=1
            
        return True
      
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        ##Edge case: 100000 or anything that ends with 0, you can find palindrome in the prefix but actually not palindrome. e.g., 1110 123210 etc.
        if x <0 or (x % 10 == 0 and x != 0):
            return False
        temp = 0
        while temp < x:
            modu = x % 10
            temp = temp*10 + modu
            x = x//10
###Edge case: odd number of digits, so 12321 123 > 21 12< 123. 
###
        if temp != x and x != temp//10:
            return False
        else:
            return True
  
