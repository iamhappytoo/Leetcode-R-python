class Solution:
    def climbStairs(self, n: int) -> int:
        sumways = 1
        if n is 1:
            return 1
        mosttwo = floor(n/2)
        for i in range(1,mosttwo+1):
            numways = n-i*2+i
            if numways == i:
                comb = 1
            else:
                comb = factorial(numways)/(factorial(i)*factorial(numways-i))
            sumways += comb
        return int(sumways)
        
