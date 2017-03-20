class Solution(object):
    # the string is actually fixed
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        S = [1,2,2]
        idx = 2
        # S:            1   22
        #                       indx
        # Occurence:    1   2   2
        # 1. Occurence String and S string are the same string,
        # therefore, based on the last digit of Occurence string (which is the indexed value, S[idx])
        # if can be figure out how many more digits need to be extended in S string (S[idx])

        # 2. The number to be extended in string S is alternative to the current last number (S[-1])
        # which is (3 - S[-1])

        # 3. indx should be incremented
        
        while len(S) < n:
            S.extend(S[idx] * [(3 - S[-1])]);
            idx += 1
        print S
        return S[:n].count(1)

print Solution().magicalString(8);
