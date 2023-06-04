# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        processed = []
        if root is None:
            return processed
        prevLevel = [root]
        nextLevel =[] 
        while True:
            processed.append(sum([i.val for i in prevLevel])/len(prevLevel))
            nextLevel = []
            for i in prevLevel:
                if i.left is not None:
                    nextLevel.append(i.left)

                if i.right is not None:
                    nextLevel.append(i.right)
            if len(nextLevel)==0:
                break
            else:
                prevLevel=nextLevel
        return processed
