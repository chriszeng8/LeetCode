class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find the number with the longest number of bits, which is the max number
        num_len = len(nums);
        if num_len<=1:
            return 0
        # pivot position to start hamming distance calculation
        bit_len = len(bin(max(nums)))-2;
        start_pos=0;

        total_hamming_dist = 0;

        def calcHammingDistance(a,b,bit_len):
            str_a = str(bin(a)[2:].zfill(bit_len));
            str_b = str(bin(b)[2:].zfill(bit_len));
            # print 'a: '+str(a) + ',b: ' + str(b);
            # print 'a: '+str_a + ',b: ' + str_b;
            return sum(str_a[i]!=str_b[i] for i in range(bit_len))

        while start_pos<len(nums)-1:
            for i in range(start_pos+1,num_len):
                total_hamming_dist = total_hamming_dist + calcHammingDistance(nums[start_pos],nums[i],bit_len);
            start_pos = start_pos+1
        return total_hamming_dist

nums = [13,2,3,3];

print Solution().totalHammingDistance(nums);
