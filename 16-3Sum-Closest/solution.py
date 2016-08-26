class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """ 
        min_diff = None
        num_len = len(nums)
        nums.sort()
        status = None
        temp_diff = 0
        min_closest_diff = sys.maxint
        closest_sum = None

        # print nums
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
                    # print "equal"
                    return temp_sum

                if (min_closest_diff>abs_diff):
                    min_closest_diff = abs_diff
                    closest_sum = temp_sum

                temp_diff =diff

        return closest_sum
