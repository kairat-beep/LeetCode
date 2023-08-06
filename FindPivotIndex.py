class Solution(object):
    def pivotIndex(self, nums):
        totSum = sum(nums)
        cumSum = 0
        if(len(nums)==0):
            return -1
        for i, val in enumerate(nums):
            if totSum - val - cumSum == cumSum:
                return i
            cumSum += val
        return -1
        
