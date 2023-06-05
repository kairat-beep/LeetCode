# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.stack = []
        self.__helper__(root)
        return self.stack
    def __helper__(self,node):
        if node is None:
            return
        self.stack.append(node.val)
        if node.left is not None:
            self.__helper__(node.left)

        if node.right is not None:
            self.__helper__(node.right)

