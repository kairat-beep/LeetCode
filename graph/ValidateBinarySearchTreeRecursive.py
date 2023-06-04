# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
MAXIMUM = float('inf')
MINIMUM = float('-inf') 
class Solution:
    def __helper__(self,ValidBST,rangeLeft,rangeRight):
        if ValidBST is None:
            return True

        if not (rangeLeft < ValidBST.val < rangeRight):
            return False

        return self.__helper__(ValidBST.left, rangeLeft, ValidBST.val) and self.__helper__(ValidBST.right, ValidBST.val, rangeRight)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.__helper__(root, MINIMUM, MAXIMUM)
