class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        zig_num =(numRows*2-2)
    	rows=['']*numRows
    	for i in range(len(s)):
    		r=min(i%zig_num,zig_num-i%zig_num)
    		rows[r]+=s[i]
    	return ('').join(rows)