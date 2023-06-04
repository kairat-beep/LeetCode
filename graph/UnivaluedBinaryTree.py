# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        needed = root.val
        def recurse(root):
            nonlocal needed
            if root is None:
                return True
            if root.val != needed:
                return False
            return recurse(root.left) and recurse(root.right)
        return recurse(root)
