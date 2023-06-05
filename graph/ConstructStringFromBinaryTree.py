# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def __helper__(root):
            if root is None:
                return None
            if root.left is None and root.right is None:
                return str(root.val)
            leftV = __helper__(root.left)
            rightV = __helper__(root.right)
            left=f"({leftV})"
            right=f"({rightV})"
            original = f"{root.val}"
            if leftV is not None:
                original += left
            else:
                original += "()"
            if rightV is not None:
                original += right
            return original

        return __helper__(root)
