# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        self.pre = float('-inf')
        return self.validBST(root)

    def validBST(self, node: TreeNode) -> bool:
        if node == None:
            return True

        if self.validBST(node.left):
            if self.pre < node.val:
                self.pre = node.val
                return self.validBST(node.right)
        return False