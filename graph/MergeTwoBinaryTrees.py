# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def combine(root1,root2):
            if root1 is None and root2 is None:
                return None

            newRoot = TreeNode()
            if root1 is not None:
               newRoot.val += root1.val

            if root2 is not None:
               newRoot.val +=root2.val

            leftL = None if root1 is None else root1.left
            rightL = None if root2 is None else root2.left
            newRoot.left = combine(leftL,rightL)
            leftR = None if root1 is None else root1.right
            rightR = None if root2 is None else root2.right
            newRoot.right = combine(leftR,rightR)
            return newRoot
        return  combine(root1,root2)

