class Solution(object):
    def threeSumClosest(self, nums, target):
        
        """
        explanation of algo:
        https://discuss.leetcode.com/topic/17215/c-solution-o-n-2-using-sort
        """ 
        min_diff = None
        num_len = len(nums)
        # sort the number array
        nums.sort()
        min_closest_diff = sys.maxint
        closest_sum = None

        for i in xrange(num_len-2):
            j = i+1
            k = num_len-1

            while (j<k):
                temp_sum  = nums[i]+nums[j]+nums[k]
                diff = temp_sum - target
                abs_diff = abs(diff)

                if (temp_sum<target):
                    j = j+1
                elif (temp_sum>target):
                    k = k-1
                else:
                    return temp_sum

                if (min_closest_diff>abs_diff):
                    min_closest_diff = abs_diff
                    closest_sum = temp_sum

        return closest_sum
