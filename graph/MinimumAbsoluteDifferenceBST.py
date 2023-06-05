# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys 
max_size = sys.maxsize
min_size = -sys.maxsize - 1 

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minimum = max_size
        def recursiveBracket(root,left,right):
            nonlocal minimum
            if root is None:
                return
            minimum = min(abs(right - root.val),abs(root.val - left), minimum)
            recursiveBracket(root.left,left,root.val)
            recursiveBracket(root.right,root.val,right)
        recursiveBracket(root.left,min_size,root.val)
        recursiveBracket(root.right,root.val,max_size)

        return minimum
