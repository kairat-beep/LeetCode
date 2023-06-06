# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def treeEqual(x,y):
            if x is None and y is None:
                return True
            if x is not None and y is not None  :
                return  x.val == y.val and treeEqual(x.left,y.left) and treeEqual(x.right,y.right)
            return False
        
        evaluate = []
        order=[[],[]]

        def inorder(orderRoot,i, target):
            nonlocal order, evaluate
            if orderRoot is None:
                return
            if target is not None and orderRoot.val == target:
                evaluate.append(orderRoot)
            inorder(orderRoot.left,i,target)
            order[i].append(orderRoot.val)
            inorder(orderRoot.right,i,target)
        inorder(root,0,subRoot.val)    
        rootOrder = order[0]
        inorder(subRoot,1, None)
        subRootOrder = order[1]

        rootString = ",".join([str(i) for i in rootOrder])
        subRootString = ",".join([str(i) for i in subRootOrder])
        result = rootString.find(subRootString)
        if result== -1:
            return False
        print("Found")
        return any( [treeEqual(subRoot,i) for i in evaluate])
