class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_len = len(nums);
        L = 0; 
        R = num_len - 1;
        sol = []
        nums.sort()
        print nums
        while (L<R):
            twoSum = nums[L]+nums[R];
            print 'twoSum: '+str(twoSum)
            if (twoSum < 0):
                # add most positive 
                for i in range(R-1, L, -1):
                    trioSum = twoSum + nums[i]
                    print 'twoSum < 0'                    
                    print 'i: '+str(i) + ' tsum: '+str(trioSum)
                    if (trioSum<0) :
                        L = L + 1
                        break
                    elif(trioSum ==0):
                        sol.append([nums[L],nums[i],nums[R]])
                        break
                # if none 3sum produces <0, or ==0 twoSum
                R = R-1
            elif (twoSum >0):
                for i in range(L+1, R):
                    trioSum = twoSum + nums[i]
                    if (trioSum>0):
                        R = R-1
                        break
                    elif (trioSum==0):
                        sol.append([nums[L],nums[i],nums[R]])
                        break
                L = L+1
            elif (twoSum ==0):
                R = R - 1
                L = L + 1
        return sol

nums = [-1, 0, 1, 2, -1, -4]
print Solution().threeSum(nums)