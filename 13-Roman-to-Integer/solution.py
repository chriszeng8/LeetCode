class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r_dict = {
        'I'  : 1,
        'IV' :4,
        'V'  :5,
        'IX' :9,
        'X' :10,
        'XL' :40,
        'L' :50,
        'XC' :90,
        'C' :100,
        'CD' :400,
        'D' :500,
        'CM' :900,
        'M' :1000
        }
        sum_s=0
        len_s = len(s)
        j=0
        while j<len_s-1:
            if s[j:j+2] in r_dict:
                sum_s=sum_s+r_dict[s[j:j+2]]   
                j=j+2
            else:
                sum_s=sum_s+r_dict[s[j]]   
                j=j+1
        if j==len_s-1:
            sum_s=sum_s+r_dict[s[j]]
        return sum_s