import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        self.max = max(nums)
        self.score = [None] * len(nums)
        self.score[0] = nums[0]
        for i in range(1, len(nums)):
            self.score[i] =  max(0, nums[i] + self.score[i-1])

    def helper(self, start, end):
        # input check
        if start > end:
            return float('-inf')
        # 1 elment array
        if start == end:
            return self.ref[start]

        # MID
        this = math.floor((start+end)/2)
        # Include mid
        left = right = 0
        if this - 1 >= start:
            left = self.getLongest(this-1, start)
        if this + 1 <= end:
            right = self.getLongest(this+1, end)
        include = left + self.ref[this] + right

        # Exclude mid
        exclude = max(self.helper(this + 1, end), self.helper(start, this - 1))

        return max([include, exclude])

    def getLongest(self, start, end):
        maximum = 0
        if start == end:
            return max([0, self.ref[start]])

        step = 1
        if start > end:
            step = -1

        accumulator = 0
        index = start
        while True:
            accumulator += self.ref[index]
            if accumulator > maximum:
                maximum = accumulator
            if index == end:
                break
            index += step

        return maximum
