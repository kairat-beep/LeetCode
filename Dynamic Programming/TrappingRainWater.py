class Solution:
    def trap(self, heights: List[int]) -> int:
        newHeights =[]
        #(LeftMaxHeight,rightMaxHeight)
        leftMax = 0
        for index, height in enumerate(heights):
            leftMax = max(leftMax,height)
            newHeights.append([leftMax,0])
        #go in reverse order
        rightMax = 0
        for index, height in reversed(list(enumerate(heights))):
            rightMax = max(rightMax,height)
            newHeights[index][1] = rightMax
            
        accum = 0
        for i in range(len(heights)):
            accum += max(0, min(newHeights[i]) - heights[i])
        return accum