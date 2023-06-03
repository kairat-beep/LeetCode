
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode])-> bool:
        return self.__helper__(root.left,root.right)
    def __helper__(self,left,right):
        p,q = left,right
        if p is None and q is  None:
            return True
        if p is not None and q is not None and p.val == q.val:
            firstHalf = self.__helper__(p.left, q.right)
            secondHalf = self.__helper__(p.right,q.left)
            return firstHalf and secondHalf 
        return False
