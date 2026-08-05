class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        min_price = prices[0]
        for i in range(1, n):
            
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                cur_profit = prices[i] - min_price
                profit = max(profit, cur_profit)    
        return profit            