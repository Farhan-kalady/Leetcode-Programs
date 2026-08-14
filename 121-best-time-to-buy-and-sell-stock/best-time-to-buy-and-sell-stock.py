class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        profit = 0
        maxi = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] < min_price:
                min_price = prices[i]
            profit = prices[i] - min_price
            maxi = max(maxi, profit) 
        return maxi       
