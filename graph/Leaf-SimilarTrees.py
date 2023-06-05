# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        output = [[],[]]
        
        def inorderLeaf(root, index):
            nonlocal output
            if root is None:
                return
            inorderLeaf(root.left,index)
            if root.left is None and root.right is None:
                output[index].append(root.val)
            inorderLeaf(root.right,index)

        inorderLeaf(root1,0)
        inorderLeaf(root2,1)
        return output[0] == output[1]

