class Solution(object):
    def totalHammingDistance(self, nums):
        # return sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)))
        print map('{:032b}'.format, nums)
        print zip(*map('{:032b}'.format, nums))
        print sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)));
        # how to prove that the contribution to hamming distance at digit n is
        # b.count('0')*b.count('1')!!!! Quite magical!!!!
nums = [13,2,3,3];

Solution().totalHammingDistance(nums);
