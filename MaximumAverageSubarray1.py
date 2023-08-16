class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current=sum(nums[0:k])
        maximum = current/k
        for index, val in enumerate(nums[k:],start=k):
            current += val - nums[index - k]
            maximum = max(maximum,current/k)
        return maximum
