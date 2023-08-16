class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mappings = dict() # The mapping array stores the last access position. Increasing updates
        mappings[nums[0]] = 0
        found = False
        for index, val in enumerate(nums[1:],1):
            if val in mappings and index - mappings[val] <= k:
                found = True
            mappings[val] = index
        return found

