from collections import defaultdict 
import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complements = set(numbers)
        for index,val in enumerate(numbers):
            if target - val in complements:
                i = bisect.bisect_left(numbers[index+1:], target-val)
                return index+1,i+index+2
