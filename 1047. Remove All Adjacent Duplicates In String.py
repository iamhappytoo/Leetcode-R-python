class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        s = list(s)
        while len(s) > 0: ##Time complexity: O(N)
            temp = s.pop(0)
            if not stack or stack[-1] != temp:
                stack.append(temp)
            else:
                stack.pop()
        
        res = ""
        for st in stack:
            res += st
        return res
##Another solution using stack time complexity: O(N), space complexity: O(N-D)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        output = []
        for ch in s:
            if output and ch == output[-1]:
                output.pop()
            else:
                output.append(ch)
                
        return ''.join(output)
