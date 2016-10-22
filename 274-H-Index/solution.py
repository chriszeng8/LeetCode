class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        cit_len = len(citations);
        if cit_len==0:
            return 0
        elif cit_len ==1:
            if citations[0]>=1:
                return 1
            else:
                return 0
        for i in range(cit_len):
            if citations[i]>= cit_len-i:
                return cit_len-i;
        return 0;