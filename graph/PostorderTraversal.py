# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root is None:
            return output
        def recursive(root):
            nonlocal output
            if root is None:
                return
            recursive(root.left)
            recursive(root.right)
            output.append(root.val)
        recursive(root)
        return output
