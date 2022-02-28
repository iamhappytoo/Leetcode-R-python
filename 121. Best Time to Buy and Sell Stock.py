class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        
        return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        diffprice = [0 for i in range(len(prices)-1)]
        for i in range(len(prices)-1):
            diffprice[i] = prices[i+1]-prices[i]
        
        i = 0
        maxprofit = 0
        cumprofit = 0
        while i < len(diffprice) and diffprice[i] < 0:
            i += 1
        if i == len(diffprice):
            return 0
        while i < len(diffprice):
            cumprofit += diffprice[i]
            maxprofit = max(maxprofit, cumprofit)
            if cumprofit < 0:
                cumprofit = 0
            i += 1
            
        return maxprofit
