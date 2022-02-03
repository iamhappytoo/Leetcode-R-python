class Solution:
    def reverseWords(self, s: str) -> str:
        right = len(s) - 1
        left = len(s) - 1
        res = []
        s = list(s)
        while left >= 0:
            if s[left] == ' ':
                while s[left] == ' ':
                    left -= 1
                    right -= 1
                res.append(s[left+1])
            else:
                while s[left] != ' ' and left >= 0:
                    left -= 1
                res.extend(s[left+1: right+1])
                right = left
        return ''.join(res).lstrip().rstrip()
                
##Another solution:
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
      
