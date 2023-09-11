class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        start = 0
        end = 0
        planted = 0
        while start < len(flowerbed):
            while start < len(flowerbed) and flowerbed[start] == 1:
                start += 1
            total = 0
            end = start
            while end < len(flowerbed) and flowerbed[end] == 0:
                end += 1
                total += 1
            if start == 0 and end >= len(flowerbed):
                return n <= math.ceil(total/2)
            elif start == 0 or end >= len(flowerbed):
                if total >= 2:
                    planted += math.floor(total / 2)
            elif total >= 3:
                planted += math.floor((total-1) / 2) 
            start = end
            end += 1
        return planted >= n

