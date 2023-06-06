# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        furthest = 1
        furthestNode = None
        if root is None:
            return 0
        def transformTree(root,parent,depth):
            if root is None:
                return
            root.parent = parent
            root.adjNodes= [root.right,root.left,parent]
            depth +=1

            transformTree(root.left, root.left,depth)
            transformTree(root.right,root.right,depth)
        tranformTree(root.left, root,1)
        tranformTree(root.right,root,1)
