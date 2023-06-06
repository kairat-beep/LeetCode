# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        minSize = sys.maxsize
        def dfsTree(root,num):
            nonlocal minSize
            if root is None:
                return
            if root.left is None and root.right is None:
                minSize = min(num+1,minSize)
                return
            dfsTree(root.right, num + 1)
            dfsTree(root.left, num + 1)
        dfsTree(root.left, 1)
        dfsTree(root.right, 1)
        return minSize
