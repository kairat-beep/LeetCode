from typing import List
import math


class Solution:

    #  values[left]  + left +  values[right] - right
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxLeft = max(values[0], values[1]+ 1)
        maxScore = values[0]  + 0 +  values[1] - 1
        lastIndex = len(values)
        i = 2
        while i < lastIndex:
            newScore  = maxLeft + values[i] - i
            if newScore>maxScore:
                maxScore  = newScore
            newLeft = i + values[i]
            if newLeft > maxLeft:
                maxLeft = i + values[i]
            i += 1
        return maxScore

Solution().maxScoreSightseeingPair([1,3,5])