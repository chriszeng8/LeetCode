class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqCount={}
        for i in nums:
            freqCount[i] =freqCount.get(i,0)+1
        return map(lambda x:x[0],sorted(freqCount.items(),key=lambda x:-x[1]))[:k]
            