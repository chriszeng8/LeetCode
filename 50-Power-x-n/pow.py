class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if (n>=0):
            if n==0:
            	return 1
            if n%2==0:
            	return self.myPow(x,n/2)*self.myPow(x,n/2);
            else:
            	return self.myPow(x,n/2)*self.myPow(x,n/2)*x;

x =3
n =10
print Solution().myPow(x,n)