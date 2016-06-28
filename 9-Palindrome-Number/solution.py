class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        half = 0
        if x==0:
            return True  
        elif (x<0) or (x%10==0):
            return False
        else:
            while (half<x):
                half,x=half*10+x%10,x/10
            return (half==x) or (half/10==x)