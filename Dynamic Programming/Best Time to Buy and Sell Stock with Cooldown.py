from typing import List
import math
class Solution:
    def helper(self):
        buy = -1 * math.inf
        sell = 0
        latestSells = [0,0]
        for price in range(self.prices):
            sell = max(sell, buy + price)
            latestSells.append(sell)
            buy = max(buy, latestSells[0] - price)
            latestSells = latestSells[1:]
        return max(sell,buy)

    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        return self.helper()
