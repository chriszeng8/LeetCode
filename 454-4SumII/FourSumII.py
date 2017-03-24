import collections

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        # all possible A+B sum count (similar to word count)
        AB = collections.Counter([a+b for a in A for b in B])
        print AB
        # Counter({0: 2, 1: 1, -1: 1})
        # minus all possible sum of C and D elements
        print [(-c-d) for c in C for d in D]

        # one thing about counter is that if such key does not exist, it will return 0 as number of count
        print [AB[-c-d] for c in C for d in D]
        
        return sum(AB[-c-d] for c in C for d in D)

A = [ 1, 2]
B = [-2,-1]
C = [0, -2]
D = [0, 2]
print Solution().fourSumCount(A,B,C,D)


# Collection Counter
# Three kinds of accepted input:

# import collections
# print collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
# print collections.Counter({'a':2, 'b':3, 'c':1})
# print collections.Counter(a=2, b=3, c=1)

# print out:
# Counter({'b': 3, 'a': 2, 'c': 1})
# Counter({'b': 3, 'a': 2, 'c': 1})
# Counter({'b': 3, 'a': 2, 'c': 1})
