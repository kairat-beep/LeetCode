import itertools
import sys

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        self.setCount = int(len(nums)/2)
        self.left = nums[:self.setCount]
        self.right = nums[self.setCount:]
        self.leftSum = sum(self.left)
        self.leftSets=[]
        self.rightSets=[]
        self.absoluteSum = sum(nums)
        self.constraintSum = self.absoluteSum / 2
        self.minimum= sys.maxsize
        self.__helper__()
        return  self.minimum
    
    def __buildLeft__(self):
        self.leftSets.append(0)
        for i in range(1, self.setCount+1):
            makeUniqueSums = set()
            for j in itertools.combinations(self.left, i):
                makeUniqueSums.add(sum(j))
            self.leftSets.append(sorted(makeUniqueSums))
    
    def __buildRight__(self):
        self.rightSets.append(0)
        for i in range(1, self.setCount+1):
            makeUniqueSums = set()
            for j in itertools.combinations(self.right, i):
                makeUniqueSums.add(sum(j))
            self.rightSets.append(sorted(makeUniqueSums))
    
    #Bug free binary search.
    #Author: Yaguang
    # https://stackoverflow.com/a/27337924/4120414
    def __binarySearch__(self, data, val):
        lo, hi = 0, len(data) - 1
        best_ind = lo
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if data[mid] < val:
                lo = mid + 1
            elif data[mid] > val:
                hi = mid - 1
            else:
                best_ind = mid
                break
            #Check if data[mid] is closer to val than data[best_ind] 
            if abs(data[mid] - val) < abs(data[best_ind] - val):
                best_ind = mid
        return data[best_ind]
    
    def __helper__(self):
        self.__buildLeft__()
        self.__buildRight__()
        difference = abs(self.absoluteSum -  2*(self.leftSum))
        if(self.minimum> difference):
            self.minimum = difference
        for i, lrow in enumerate(self.leftSets[1:self.setCount], start = 1):
            for lvalue in lrow:
                rvalue = self.__binarySearch__(self.rightSets[self.setCount - i], self.constraintSum - lvalue)
                difference = abs(self.absoluteSum -  2*(lvalue + rvalue))
                if self.minimum > difference:
                    self.minimum = difference
