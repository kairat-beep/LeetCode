from collections import defaultdict 
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(node):
            nonlocal graph
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    dfs(i)
                
        dfs(source)
        return destination in visited
