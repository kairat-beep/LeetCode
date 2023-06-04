# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def search(root, original,target):
            if root is None:
                return None
            if original == target:
                return root
            left = search(root.left, original.left, target)
            right = search(root.right, original.right ,target)
            found = None
            if left is not None:
                found = left
            if right is not None:
                found = right
            return found
        return search(cloned,original,target)
