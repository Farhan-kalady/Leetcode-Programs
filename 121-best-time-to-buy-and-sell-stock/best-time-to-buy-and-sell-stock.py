class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        profit = 0
        total = 0
        for i in range(1,len(prices)):
            profit = prices[i] - min_price
            if prices[i] < min_price:
                min_price = prices[i]
            total = max(total, profit)     
        return total         
