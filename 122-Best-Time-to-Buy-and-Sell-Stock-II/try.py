class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # when to buy?
        # 1. when not holding any stock (i.e., sold = true)
        # 2. when the price is local minimal

        # when to sell?
        # 1. 
        # 2. 

        # find all the local minima and maxima.
        # then pair them.

        # bool variable: whether stocks are sold or not?
        # if current value is local minimum (valley):
        # if the current value is less than the previous value and the next is larger than current
        profit = 0;
        num_len = len(prices);
        # local minimum
        for i in range(num_len-1):
        	price_inc = prices[i+1] - prices[i]
        	if (price_inc > 0):
        		profit = profit + price_inc
        return profit

prices = [98, 99, 100.1, 70, 75, 76, 75, 70, 75, 93, 100]
a = Solution()
print a.maxProfit(prices)