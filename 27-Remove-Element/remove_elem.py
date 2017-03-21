class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # sort list
        nums.sort()
        start,end = None,None

        num_len = len(nums)
        
        val_appeared = False
        for i in range(num_len):
        	# first time value appear
        	if (nums[i]==val) and (val_appeared==False):
        		start = i
        		end = start
        		val_appeared = True
        	elif (nums[i]==val):
        		end = i

        if val_appeared:
	        counter = 0
	        for j in nums[end+1:num_len]:
	        	nums[start+counter]=j
	        	counter = counter +1
	        return nums[:start+counter]
        else:
	    	return nums



nums=[3,2,2,4,3]
val = 3
print Solution().removeElement(nums,val)