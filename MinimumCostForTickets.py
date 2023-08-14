import sys
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        charge = [0]* (max(days) + 1)
        pick = set(days)
        for index in range(1, max(days) + 1):
            if index not in pick:
                charge[index] = charge[index-1]
                continue
            charge[index] = min([(charge[index - days] + price) if (index - days) >= 0 else price for (price, days) in zip(costs, [1, 7, 30]) ])
        return charge[-1]
