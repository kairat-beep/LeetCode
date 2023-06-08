class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        visited = set()
        for i,j in edges:
            if i in visited:
                return i
            if j in visited:
                return j
            visited.add(i)
            visited.add(j)
        return -1
