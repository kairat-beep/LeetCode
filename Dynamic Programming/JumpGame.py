from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        boundary = 0
        i = 0
        while i < size:
            if  i > boundary:
                break
            end = i + nums[i] 
            if end > boundary:
                boundary = end
            i += 1
        return boundary >= size - 1