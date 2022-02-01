class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        #transform
        #Easier to interpret with 1 can pass/ 0 can't
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                obstacleGrid[i][j] =  1 - obstacleGrid[i][j]
        #clear the first row
        start0 = 0
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 0:
                start0= 1
            if start0 == 1:
                obstacleGrid[0][i] = 0
        
        for i in range(1, len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    continue
                left = 0
                if j != 0:
                    left = obstacleGrid[i][j - 1]
                top = obstacleGrid[i-1][j]
                obstacleGrid[i][j] = left + top
        return obstacleGrid[-1][-1]