from random import randint

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums;

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original;

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        # Make a copy of list use[:]!!!!!
        rand_list = self.original[:]; # make a copy of the list
        for i in range(len(rand_list)): # from the start
            j = randint(i,len(rand_list)-1);
            rand_list[i],rand_list[j] = rand_list[j], rand_list[i]
        return rand_list

nums = [1,2,3,4,5,6,7];
solution = Solution(nums);
print solution.reset();
print solution.shuffle();

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
