class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        counter = 0
        num_strs = len(strs)
        if (num_strs==0):
            return ''
        elif (num_strs==1):
            return strs[0]
    
        # shortest length among all strings
        shortest_length = min(map(len,strs))
        if (shortest_length==0):
            return ''

        # print strs
        # print 'shortest_length: '+str(shortest_length)
    
        for i in range(shortest_length):
            #store the first character 
            # i is character
            str_i_0=strs[0][i]
            # print 'str_i_0: '+str_i_0
    
            all_equal = True
            # j: word idex
            for j in range(1,num_strs):
                # print 'j: '+str(j)
                # print 'strs[j][i]: '+strs[j][i]
                if strs[j][i]!=str_i_0:
                    all_equal = False
                    break
            if (all_equal == True):
                counter = counter+1
            else:
    
                break
        return strs[0][:counter]