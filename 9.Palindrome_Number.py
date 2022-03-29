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
      
  
