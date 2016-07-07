class Solution(object):
    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0 or len(s)==1: 
        	return len(s)
        left=0
        right=1
        charDict = {}
        charDict[s[left]]=left
        LongestStrLen =1
        while right<len(s):
        	# if the right most character is already in the hashmap
        	# currently found temporary longest substring
        	if s[right] in charDict:
        		left = max(left,charDict[s[right]]+1)
        
        	if (right-left)+1>LongestStrLen:
        		LongestStrLen=right-left+1
        	charDict[s[right]] = right
        	right=right+1
        
        return LongestStrLen
