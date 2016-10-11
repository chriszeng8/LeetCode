class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums);
        if num_len<= 1:
            return num_len
        prev_diff = nums[1] - nums[0]
        if (prev_diff!=0):
            sign_flip_counter = 1
        else:
            sign_flip_counter = 0

        for i in range(1, num_len-1):
            diff = nums[i+1] - nums[i];
            if diff == 0:
            	continue
            elif (diff * prev_diff <= 0):
                sign_flip_counter = sign_flip_counter + 1
            prev_diff = diff;
        return sign_flip_counter+1;
