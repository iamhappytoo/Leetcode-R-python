class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lisstr = ['' for i in range(numRows)]
        i = 0
        div = numRows - 1
        while i < len(s):
            col = i//div
            row = i % div
            if col % 2 == 0:
                lisstr[row] += s[i]
            else:
                lisstr[numRows-row-1] += s[i]
            
            i += 1
            
        output = ''
        for i in range(numRows):
            output += str(lisstr[i])
            
        return output
