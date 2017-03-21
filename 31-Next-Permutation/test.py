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
                    diff = 999;
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
        print nums
# 1,3,2,0,4,2,1
# 1,3,2,1,0,2,4

nums = [1,3,2]
nums = [1,3,2,0,4,2,0]
nums = [2,2,7,5,4,3,2,2,1]
nums = [11,12,0,27,3,11,21,9,0,15,26,27,17,24,0,16,4,17,14,8,15,8,2,16,10,6,6,24,16,2,18,19,6,10,17,10,21,0,11,13,7,7,2,16,24,25,2,20,12,9,20,19]
a = Solution()
a.nextPermutation(nums)