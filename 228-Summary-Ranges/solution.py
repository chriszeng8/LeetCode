class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        num_len = len(nums);
        range_list = [];
        
        if num_len == 0:
            return range_list;
        elif num_len ==1:
            range_list.append(str(nums[0]));
            return range_list;
        
        # initialization
        prev = nums[0]
        rng_start = prev
        rng_end = prev

        # loop thru to the second last elem
        for i in range(1,num_len-1):
            if (nums[i]==prev+1):
                rng_end = nums[i]
            else:
                if rng_start == rng_end:
                    range_list.append(str(rng_start));
                else:
                    range_list.append(str(rng_start)+'->'+str(rng_end));
                rng_start = nums[i]
                rng_end = nums[i]
            prev = nums[i]

        # condition on the very last elem individually, as the closing condition may vary.

        if (nums[num_len-1]==prev+1):
            range_list.append(str(rng_start)+'->'+str(nums[num_len-1]));
        else:
            if rng_start == rng_end:
                range_list.append(str(rng_start));
            else:
                range_list.append(str(rng_start)+'->'+str(rng_end));
            range_list.append(str(nums[num_len-1]));
        return range_list; 
