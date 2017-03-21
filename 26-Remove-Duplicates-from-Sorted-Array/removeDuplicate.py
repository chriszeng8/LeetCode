class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums) 
        if num_len<=1:
        	return(num_len)
        # store the largest num
        largest_num = nums[0]
        counter = 1
        for i in range(1,num_len):
        	if nums[i]>largest_num:
        		largest_num = nums[i]
        		nums[counter] = nums[i]
        		counter = counter + 1
        # nums = nums[:counter]
        print nums
        return counter

nums = [10,10,20,20,30]
print Solution().removeDuplicates(nums)