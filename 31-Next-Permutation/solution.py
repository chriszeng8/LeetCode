class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_len = len(nums)
        if ((nums == sorted(nums,reverse = True)) or (num_len==1)):
            nums.sort()
        else:
            for i in range(num_len-1,-1,-1):
                if nums[i-1] < nums[i]:
                    # temp store the smallest value
                    diff = 999
                    swap_index = i
                    # find the list element that is just larger than to-be-swapped front digit[i-1]
                    for j in range(i,num_len):
                    	temp_diff = nums[j] - nums[i-1]
                    	if (temp_diff>0) and (temp_diff<diff):
                    		diff = temp_diff
                    		swap_index = j
                    temp = nums[swap_index]
                    nums[swap_index] = nums[i-1]
                    nums[i-1] = temp
                    nums[i:num_len] = sorted(nums[i:num_len])
                    break
