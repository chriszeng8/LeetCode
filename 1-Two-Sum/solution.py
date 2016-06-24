class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        range_num = range(len(nums))
        for i in range_num:
            for j in range_num[i+1:]:
                if (nums[i]+nums[j]==target):
                    return [i,j]