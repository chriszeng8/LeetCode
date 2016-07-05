class Solution(object):
    def longestPalindrome(self,s):
        """
        :type s: str
        :rtype: str
        """
        templongStr = 1
        str_len = len(s)
        longestStart=0
        longestEnd=0
        
        for i in range(str_len)[:-1:]:
            start = i
            end = i+1
            while (start>=0) and (end<str_len) and (s[start]==s[end]):
                if (end-start)+1 > templongStr:
                    templongStr = end-start+1 
                    longestStart = start
                    longestEnd = end
                start=start-1
                end= end+1
    
            start = i-1
            end = i+1
    
    
            while (start>=0) and (end<str_len) and (s[start]==s[end]):
                if (end-start)+1 > templongStr:
                    templongStr = end-start
                    longestStart = start
                    longestEnd = end
                start=start-1
                end= end+1
            
        return s[longestStart:longestEnd+1]