class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        counted = 0
        #Find the first cell
        LAND = 1
        maxCol, maxRow = len(grid[0]), len(grid)
        visited = set()
        def findFirst(grid):
            for rowi, row in enumerate(grid):
                for coli, col in enumerate(row):
                    if col == LAND:
                        return (rowi,coli)

        def dfs(location):
            nonlocal counted, visited, grid, maxCol, maxRow, LAND 
            (row, col) = location
            if(row,col) in visited:
                return
            if 0>row or row>=maxRow:
                return
            if 0>col or col >=maxCol:
                return
            if grid[row][col] == 0:
                return
            visited.add((row,col))

            #Check 4 sides
            #upper
            if row == 0 or row > 0 and (0 == grid[row-1][col]):
                counted +=1
            if col == 0 or col > 0 and (0 == grid[row][col-1]):
                counted +=1
            if col == maxCol - 1 or col < maxCol-1 and (0== grid[row][col+1]):
                counted +=1 
            if row == maxRow - 1 or row < maxRow-1 and (0 == grid[row+1][col]):
                counted +=1

            dfs((row-1,col))
            dfs((row,col-1))
            dfs((row+1,col))
            dfs((row,col+1))            
            
        dfs(findFirst(grid))
        return counted
