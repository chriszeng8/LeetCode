class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0;
        num_len = len(prices);
        # local minimum
        for i in range(num_len-1):
        	price_inc = prices[i+1] - prices[i]
        	if (price_inc > 0):
        		profit = profit + price_inc
        return profit