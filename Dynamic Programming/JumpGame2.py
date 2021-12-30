from typing import List

class Solution:
    def jump(self, nums: List[int]) -> bool:
        size = len(nums)
        positions = list(range(size))
        start = end = 0
        counter = 0
        while end < size - 1:
            counter += 1
            steps = nums[start : end + 1 : 1]
            rng = positions[start : end + 1 : 1]
            start = end + 1
            end = max([x + y for x, y in zip(steps, rng)])
        return counter