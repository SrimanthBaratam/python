class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum=prices[0]
        profit=0
        for i in range(len(prices)):
            minimum=min(minimum,prices[i])
            profit=max(profit,prices[i]-minimum)
        return profit