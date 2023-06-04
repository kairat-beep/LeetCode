class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(__helper__(root.left,1),__helper__(root.right,1))
        def __helper__(subRoot, depth):
            if subRoot is None:
                return depth
            return max(__helper__(subRoot.left, depth+1 ), __helper__(subRoot.right, depth+1))
