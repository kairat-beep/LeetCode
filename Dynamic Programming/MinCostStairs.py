from itertools import repeat
import sys


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cumCost = list(repeat(sys.maxsize, len(cost)))
        cumCost[0], cumCost[1] = 0, 0
        for i in range(2, len(cost)):
            if cumCost[i] > cumCost[i-1] + cost[i-1] or cumCost[i] > cumCost[i-2] + cost[i-2]:
                cumCost[i] = min(cumCost[i-1] + cost[i-1],
                                 cumCost[i-2] + cost[i-2])
        return min(cumCost[-1]+cost[-1], cumCost[-2]+cost[-2])
