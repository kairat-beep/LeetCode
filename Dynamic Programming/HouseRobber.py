class Solution:
    def rob(self, nums: List[int]) -> int:
        self.d = dict()
        return self.helper(nums)
        
    def helper(self,nums):
        sizeOf = len(nums)
        if(sizeOf in self.d):
            return self.d[sizeOf]
        
        if sizeOf <= 2:
            self.d[sizeOf]= max(nums)
            return self.d[sizeOf]
        include = self.helper(nums[2:])
        exclude = self.helper(nums[1:])

        self.d[sizeOf] = max(include + nums[0], exclude)
        return self.d[sizeOf]
        