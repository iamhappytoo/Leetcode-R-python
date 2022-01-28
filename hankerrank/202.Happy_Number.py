class Solution:
    def isHappy(self, n: int) -> bool:
        
        sethas = set()
        while n != 1:
            if n in sethas:
                return False
            sethas.add(n)
            s = str(n)
            Sum = 0
            for num in s:
                Sum += int(num)*int(num)
            n = Sum
        
        return True
