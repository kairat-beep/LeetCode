"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        original = []

        def __helper__(node):
            if node is not None:
                original.append(node.val)
                for i in node.children:
                    __helper__(i)
        __helper__(root)
        return original

