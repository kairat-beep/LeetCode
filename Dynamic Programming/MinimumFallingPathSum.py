import sys
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        width = len(matrix[0])
        height = len(matrix)
        for i in range(1, height):
            for j in range(width):
                #checkLeft
                left = sys.maxint
                if j > 0:
                    left = matrix[i - 1][j - 1]
                #checkTop
                top = sys.maxint
                top = matrix[i - 1][j]
                #checkRight
                right = sys.maxint
                if j < width - 1:
                    right = matrix[i - 1][j + 1]

                matrix[i][j] += min(left,top,right)
        return min(matrix[-1])