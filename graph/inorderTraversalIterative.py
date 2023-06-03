class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        inorder = []
        if root is None:
            return inorder
        stack.append(root)
        while len(stack)>0:

            while stack[-1].left is not None:
                left = stack[-1].left
                stack[-1].left = None
                stack.append(left)

            node = stack.pop()
            inorder.append(node.val)


            if node.right is not None:
                stack.append(node.right)

        return inorder
