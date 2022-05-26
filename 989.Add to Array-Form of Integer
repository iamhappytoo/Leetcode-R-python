class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        karray = []
        while k > 0:
            karray.append(k % 10)
            k = k//10
        karray = karray[::-1]
        
        ##element-wise addition
        pta = len(num)-1
        ptb = len(karray)-1
        carry = 0
        
        answer = []
        while pta >= 0 or ptb >= 0:
            x = num[pta] if pta >= 0 else 0
            y = karray[ptb] if ptb >= 0 else 0
            answer.append((x + y + carry) % 10)
            carry = (x + y + carry) // 10
            pta -= 1
            ptb -= 1
            
        if carry:
            answer.append(carry)
        return answer[::-1]
Deficiency: time complexity max(len(num), logK), need two array.
##A quicker way of add with smaller spatial complexity, need only one array
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num)-1, -1, -1):
            if not k: break
            k, num[i] = divmod(num[i]+k, 10)
        
        while k:
            k, a = divmod(k, 10)
            num = [a] + num
            
        return num
