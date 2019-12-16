# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return None
        
        lis = []
        lis.append([root.val])
        self.appendList(root.left, 1, lis)
        self.appendList(root.right, 1, lis)
        
        return lis
        
    def appendList(self, node:TreeNode, level:int, lis):
        if not node:
            return
        
        if level > len(lis) - 1:
            lis.append([node.val])
        else:
            lis[level].append(node.val)
        
        self.appendList(node.left, level + 1, lis)
        self.appendList(node.right, level + 1, lis)
