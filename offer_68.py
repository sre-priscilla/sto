# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or root is p or root is q:
            return root
        lca = self.lowestCommonAncestor(root.left, p, q)
        rca = self.lowestCommonAncestor(root.right, p, q)
        if lca is None:
            return rca
        if rca is None:
            return lca
        return root