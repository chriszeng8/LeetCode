class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if (len(matrix)==0) or (len(matrix[0])==0):
            return;
        self.cumMatrix = [[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)];

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.cumMatrix[i+1][j+1] = self.cumMatrix[i][j+1]+self.cumMatrix[i+1][j]+matrix[i][j] - self.cumMatrix[i][j];

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.cumMatrix[row1][col1]+self.cumMatrix[row2+1][col2+1]-self.cumMatrix[row2+1][col1]-self.cumMatrix[row1][col2+1]; 


# matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

matrix = [[-4,-5]]

# Your NumMatrix object will be instantiated and called as such:
numMatrix = NumMatrix(matrix);
# print numMatrix.sumRegion(2, 1, 4, 3)
print numMatrix.sumRegion(0,0,0,0);
print numMatrix.sumRegion(0,0,0,1);
print numMatrix.sumRegion(0,1,0,1)
# numMatrix.sumRegion(1, 2, 3, 4)
