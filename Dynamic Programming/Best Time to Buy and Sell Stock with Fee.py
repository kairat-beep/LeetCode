from typing import List
import math
class Solution:
    def helper(self):
        buy = -1 * math.inf
        sell = 0
        for price in self.prices:
            sell = max(sell, buy + price)
            buy = max(buy, sell - price - self.fee)
        return max(sell,buy)

    def maxProfit(self, prices: List[int], fee: int) -> int:
        self.prices = prices
        self.fee = fee
        return self.helper()
