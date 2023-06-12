# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NotBalanced(Exception):
    pass

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def __balance__(root):
            if root is None:
                return 0
            
            ## Leaf
            if root.left is None and root.right is None:
                return 1
            
            left = __balance__(root.left)
            right = __balance__(root.right)
            if (abs((max(left,right)-min(left,right))) > 1):
                raise  NotBalanced()
            return max(left,right) + 1
            
        balanced = True

        try:
            __balance__(root)
        except NotBalanced:
            balanced = False
        return balanced


