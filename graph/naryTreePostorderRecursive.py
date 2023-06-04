"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        original = []

        def __helper__(node):
            if node is not None:
                for i in node.children:
                    __helper__(i)
                original.append(node.val)
        __helper__(root)
        return original
