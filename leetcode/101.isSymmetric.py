# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        return self.comparelist(root.left,root.right)
    
    def comparelist(self, lnode:TreeNode, rnode:TreeNode) -> bool:
        if lnode == None and rnode == None:
            return True
        
        if lnode==None and rnode!=None:
            return False
        
        if lnode !=None and rnode == None:
            return False
        
        if lnode.val != rnode.val:
            return False
        
        return self.comparelist(lnode.left, rnode.right) and self.comparelist(lnode.right, rnode.left)
        
