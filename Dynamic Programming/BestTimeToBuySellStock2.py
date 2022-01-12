from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitAccum = 0
        lastIndex = len(prices)
        i = 1
        while i < lastIndex:
            if prices[i] - prices[i-1] > 0:
                profitAccum += prices[i] - prices[i-1]
            i += 1
        return profitAccum
