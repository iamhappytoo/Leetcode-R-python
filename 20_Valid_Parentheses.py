class Solution:
    def isValid(self, s: str) -> bool:
        s=list(s)
        def close(q,p):
            if q == '(' and p == ')':
                return True
            if q == '{' and p == "}":
                return True
            if q == "[" and p == "]":
                return True
            return False
                
        q = []
        while len(s)> 0:
            temp = s.pop(0)
            if len(q) == 0:
                q.append(temp)
            else:
                if close(q[-1],temp):
                    q.pop()
                else:
                    q.append(temp)
        
        if len(q)>0:
            return False
        else:
            return True

          
#Another solution:
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
