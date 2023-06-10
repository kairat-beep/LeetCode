# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0

        if root is None:
            return longest 

        def transformTree(node,parent):
            if node is None:
                return

            node.adjNodes= [ i for i in [node.right,node.left, parent] if i is not None]
            transformTree(node.left, node)
            transformTree(node.right, node)

        transformTree(root,None)

        visited = set()
        theLast = root
        keepRunning = True
        def DFS(node,depth):
            nonlocal longest, visited, keepRunning, theLast
            visited.add(node)
            if depth > longest:
                keepRunning = True
                theLast = node
                longest = depth

            for i in [ _ for _ in node.adjNodes if _ not in visited]:
                visited.add(i)
                DFS(i, depth+1)
        while keepRunning:
            keepRunning = False
            DFS(theLast, 0)
            visited = set()

        return longest 

