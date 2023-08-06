import sys
 
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        b = sys.maxsize
        a = nums[0]
        for i in nums[1:]:
            if (a < b < i):
                return True 
            a = min(a,i)
            if (i > a):
                b = min(b,i)
        return False
