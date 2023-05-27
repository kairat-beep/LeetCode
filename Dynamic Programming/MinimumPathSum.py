class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #Keep 1 row to save memory
        temporal = grid[0].copy()
        for i in range(1,len(grid[0])):
            temporal[i]+=temporal[i-1]

        #Pick the min of the Top or Left Cell.
        for row in grid[1:]:
            temporal[0] += row[0]
            for index in range(1, len(row)):
                temporal[index] = min(temporal[index-1],temporal[index]) + row[index]
        return temporal[-1]

