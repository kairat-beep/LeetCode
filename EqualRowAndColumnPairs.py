from collections import defaultdict 
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        records = defaultdict(int)

        for index, row  in enumerate(grid):
            records[hash(tuple(row))] += 1
        
        collected = 0
        for colI in range(len(grid[0])):
            record =hash(tuple([i[colI] for i in grid]))
            collected += records[record]

        return collected


