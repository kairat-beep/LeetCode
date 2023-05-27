import sys
class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.totalSum = sum(nums)
        self.setCount = len(nums)/2
        self.minimum = sys.maxsize
        self.nums = nums
        self.__helper__(0, 0, 0)
        return self.minimum

    def __helper__(self, set1size, position, currentSum):
        if self.setCount == position - set1size:
            theRest = sum(self.nums[position:])
            self.minimum = min(self.minimum, abs(self.totalSum - 2 * currentSum - 2 * theRest))
            return
        if set1size == self.setCount:
            self.minimum = min(self.minimum, abs(self.totalSum - 2 * currentSum))
            return 
        #Two sets: 1 and 2.
        #Place the current Number to the Set 1
        self.__helper__(set1size + 1, position + 1, currentSum + self.nums[position])
        #Place the current Number to the Set 2
        self.__helper__(set1size, position + 1, currentSum)
print(Solution().minimumDifference([7772197,4460211,-7641449,-8856364,546755,-3673029,527497,-9392076,3130315,-5309187,-4781283,5919119,3093450,1132720,6380128,-3954678,-1651499,-7944388,-3056827,1610628,7711173,6595873,302974,7656726,-2572679,0,2121026,-5743797,-8897395,-9699694]))
