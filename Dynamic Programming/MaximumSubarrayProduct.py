import math
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product = nums[0]
        maxProduct = negProduct = 1
        for i in range(0,len(nums)):
            maxProduct, negProduct = max(nums[i], nums[i] *maxProduct, nums[i] * negProduct),min(nums[i], nums[i] *maxProduct, nums[i] * negProduct)
            product = max(product,maxProduct,negProduct)
        return product