class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price = prices[0]

        for i in prices:
            min_price = min(min_price, i)
            profit = max(profit, i - min_price)

        return profit    
