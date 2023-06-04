# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        leftMost = None
        head = root
        stack = [root]
        prev = None 
        while 0 != len(stack):
            #All the way to the left
            while stack[-1].left is not None:
                tmp = stack[-1].left
                stack[-1].left = None
                stack.append(tmp)
            head = stack.pop()
            
            #New root
            if leftMost is None:
                leftMost = head
            else:
                prev.right = head
            prev = head

            #Append the right child OR 
            # process right child of the parent
            if head.right is not None:
                stack.append(head.right)
        return leftMost
