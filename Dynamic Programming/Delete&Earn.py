from typing import List
from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        self.d = dict()
        self.weights = {key: key * value for (key, value) in Counter(nums).items()}
        return self.deleteAndEarnHelper(sorted(set(nums)))
        
    def deleteAndEarnHelper(self,nums):
        sizeOf = len(nums)
        if(sizeOf in self.d):
            return self.d[sizeOf]
        if sizeOf == 0:
            self.d[sizeOf] = 0
            return self.d[sizeOf]
        if sizeOf == 1:
            self.d[sizeOf] = self.weights[nums[0]]
            return self.d[sizeOf]

        curNum = nums[0]
        #Include
        if nums[1] == curNum + 1:
            include = self.deleteAndEarnHelper(nums[2:])
        else:
            include = self.deleteAndEarnHelper(nums[1:])

        #Exclude
        exclude = self.deleteAndEarnHelper(nums[1:])

        self.d[sizeOf] = max(include + self.weights[curNum], include + self.weights[curNum], exclude)
        return self.d[sizeOf]