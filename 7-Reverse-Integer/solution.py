class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            sign = -1
            x = -x
        else:
            sign = 1
        new_int=0
        
        while x>9:
            new_int=new_int*10+x%10
            x=x/10
        if x!=0:
            new_int=new_int*10+x
        if new_int>=2147483647:
            return 0
            
        return new_int*sign
