"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        def recursive(root,num):
            if root is None:
                return num
            if len(root.children) == 0:
                return num+1
            return max([recursive(i,num+1) for i in root.children ])
        return recursive(root,0)

