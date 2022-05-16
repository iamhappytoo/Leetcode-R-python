class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p1 = len(a) - 1
        p2 = len(b) - 1
        carry = 0
        sumStr = ''
        
        while p1 >= 0 or p2 >= 0:
            x1 = int(a[p1]) if p1 >= 0 else 0
            x2 = int(b[p2]) if p2 >= 0 else 0
            
            value = (x1 + x2 + carry) % 2
            carry = (x1 + x2 + carry) // 2
            
            sumStr += str(value)
            p1 -= 1
            p2 -= 1
            
        if carry:
            sumStr += str(carry)
        
        return sumStr[::-1]
      
##Simpler solution using built-in format function
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a,2)+int(b,2))

##Another way of bit-by-bit computation of string
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        
        carry = 0
        answer = ''
        
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
                
            answer += str(carry % 2)
            
            carry //= 2
        
        if carry:
            answer += '1'
        
        return answer[::-1]
      
##bit manipulation XOR and OR loop 
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]
      
