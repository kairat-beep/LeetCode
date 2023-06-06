# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None :
            return False

        def dfsTree(node,curr):
            nonlocal targetSum
            
            if node.left is None and node.right is None:
                return curr +node.val== targetSum

            response = False
            if (node.left is not None):
                response = dfsTree(node.left, curr+node.val) 
            if (node.right is not None):
                response |= dfsTree(node.right, curr+node.val)
            return  response

        return dfsTree(root,0)
