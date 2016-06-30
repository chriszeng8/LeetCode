class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        heightsize = len(height)
        left = 0
        right = heightsize-1
        #calculate the initial areaMax
        minHeight= height[right] if (height[right]<height[left]) else height[left]
        tempMax=(right-left)*minHeight
        
        while (left<right):
            if height[left]>height[right]:
                right=right-1;
            else:
                left=left+1;
            minHeight= height[right] if (height[right]<height[left]) else height[left]
            areaMax=(right-left)*minHeight
            if areaMax>tempMax:
                tempMax=areaMax;
            
        return tempMax;