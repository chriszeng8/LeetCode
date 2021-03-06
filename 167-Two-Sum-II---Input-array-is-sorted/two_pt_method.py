class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_len = len(numbers);
        rightPt = num_len -1;
        leftPt = 0;

        #if sum of right and left points is less than target
        # move the leftpt one element forward (to the right),
        # rightpt element remain the same.
        while leftPt<rightPt:
        	tmp_sum = numbers[leftPt] + numbers[rightPt]
        	if (tmp_sum == target):
        		return (leftPt, rightPt)
        	elif (tmp_sum < target):
        		leftPt = leftPt + 1
        	else:
        		rightPt = rightPt -1


nums = [1,2,4,5,6,8]
target = 8
a = Solution();
print a.twoSum(nums, target);