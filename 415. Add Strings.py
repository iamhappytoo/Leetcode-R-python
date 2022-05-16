class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        pt1 = len(num1) - 1
        pt2 = len(num2) - 1
        sumStr = ""
        add = 0
        while pt1 >= 0 and pt2 >= 0:
            Sum = int(num1[pt1]) + int(num2[pt2]) + add
            res = Sum % 10
            add = Sum // 10
            sumStr += str(res)
            pt1 -= 1
            pt2 -= 1
        while pt1 >= 0:
            Sum = int(num1[pt1]) + add
            res = Sum % 10
            add = Sum // 10
            sumStr += str(res)
            pt1 -= 1
        
        while pt2 >= 0:
            Sum = int(num2[pt2]) + add
            res = Sum % 10
            add = Sum // 10
            sumStr += str(res)
            pt2 -= 1
        while add > 0:
            sumStr += str(add)
            add = add // 10
            
        outStr = sumStr[::-1]
        return outStr
      
      
##A shorter code
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sumStr = ''
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry = 0
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1])-ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2])-ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            sumStr += str(value)
            p1 -= 1
            p2 -= 1
        
        if carry:
            sumStr += str(carry)
        
        return sumStr[::-1]
