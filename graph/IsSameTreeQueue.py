# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue

class Solution:
    def isSameTree(self, p1: Optional[TreeNode], p2: Optional[TreeNode]) -> bool:
        try:
            q = queue.Queue()
            
            if p1 is None and p2 is None:
                return True
            if p1 is None or p2 is None:
                 return False
            
            q.put((p1,p2))
            
            while not q.empty():
                a,b = q.get()
                if a is None and b is None:
                    continue

                if a is None and b is not None  or a is not None and b is None or a.val != b.val:
                    raise Exception('tree is not same')

                if(a.left or b.left):
                    q.put((a.left,b.left))
                if(a.right or b.right):
                    q.put((a.right,b.right))
        except:
            return False
        return True
