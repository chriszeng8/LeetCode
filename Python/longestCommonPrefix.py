def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    counter = 0
    num_strs = len(strs)

    # shortest length among all strings
    shortest_length = min(map(len,strs))
    # print strs
    # print 'shortest_length: '+str(shortest_length)


    for i in range(shortest_length):
    	#store the first character 
    	# i is character
    	str_i_0=strs[0][i]
    	print 'str_i_0: '+str_i_0

    	all_equal = True
    	# j: word idex
    	for j in range(1,num_strs):
    		print 'j: '+str(j)
    		print 'strs[j][i]: '+strs[j][i]
    		if strs[j][i]!=str_i_0:
    			all_equal = False
    			break
    	if (all_equal == True):
    		counter = counter+1
    	else:

    		break

    return strs[0][:counter]

strs=['ce','ce','ce'];    	
print longestCommonPrefix(strs)