class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        cumSum = 0
        maxAlt = 0
        for i in gain:
            cumSum += i
            maxAlt = max(cumSum,maxAlt)
        return maxAlt
