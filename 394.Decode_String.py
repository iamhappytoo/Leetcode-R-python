class Solution:
    def decodeString(self, s: str) -> str:
        countStack = []
        stringStack = []
        currentString = ""
        k = 0
        for ch in s:
            if ch.isdigit():
                k = k*10 + int(ch)
            elif ch == '[':
                countStack.append(k)
                stringStack.append(currentString)
                currentString = ""
                k = 0
            elif ch == ']':
                decodedString = stringStack[-1]
                for i in range(countStack[-1]):
                    decodedString += currentString
                stringStack.pop()
                countStack.pop()
                currentString = decodedString
            else:
                currentString += ch
        
        return currentString
      
      
##Time complexity: O(maxK*n), n is the size of the string, and k is the max number. 
##Space complexity: O(m+n), m is the number of alphabets, and n is the number of digits. for store in the stack, and other constant space for storing the strings and current K.
