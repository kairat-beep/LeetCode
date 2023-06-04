# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        total = 0

        def sumToLeaf(root, original):
            nonlocal total
            if root is None:
                total += original
                return
            original <<=1
            original += root.val
            sumToLeaf(root.left, original)
            sumToLeaf(root.right, original)
        sumToLeaf(root,0)
        return total
