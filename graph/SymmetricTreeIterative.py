import queue

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = queue.Queue()
        if root is not None:
            q.put((root.left,root.right))
        else:
            return True
        while not q.empty():
            left, right = q.get() 

            if left is None and right is None:
                continue
            
            if left is not None and right is not None:
                if left.val == right.val:
                    q.put((left.left,right.right))
                    q.put((left.right,right.left))
                    continue
                else:
                    return False
            else:
                return False
            return False
        return True
