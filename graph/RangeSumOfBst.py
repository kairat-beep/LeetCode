# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        def recursive(root, low, high):
            nonlocal total
            if root is  None:
                return
            if (low<=root.val<=high):
                total = total + root.val

            recursive(root.left,low,high)
            recursive(root.right,low,high)
        recursive(root,low,high)
        return total
