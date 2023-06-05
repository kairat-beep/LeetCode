# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return false
        treeNums= {root.val}
        def dfsTree(root) :
            nonlocal treeNums, k
            if root is None:
                return False

            if (k - root.val) in treeNums:
                return True
            treeNums.add(root.val)
            return dfsTree(root.left) or dfsTree(root.right)

        return dfsTree(root.left) or dfsTree(root.right)
