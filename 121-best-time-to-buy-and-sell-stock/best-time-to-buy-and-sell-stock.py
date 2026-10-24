class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=prices[0]
        max_profit=0
        for n in prices:
            if n<buy:
                buy=n
            profit = n-buy
            if profit>max_profit:
                max_profit = profit
        return max_profit