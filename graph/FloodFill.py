class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        original = image[sr][sc]
        def dfs(location,image, color):
            nonlocal visited, original
            maxCol, maxRow = len(image[0]), len(image)
            if location in visited:
                return
            visited.add(location)
            (row, col) = location

            if 0>row or row>=maxRow:
                return
            if 0>col or col >=maxCol:
                return
            if image[row][col]  != original:
                return

            
            image[row][col] = color

            dfs((row-1,col),image,color)
            dfs((row+1,col),image,color)
            dfs((row,col-1),image,color)
            dfs((row,col+1),image,color)          
                
        dfs((sr,sc),image, color)
        return image

