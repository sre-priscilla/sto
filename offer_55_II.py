# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def isBalanced(self, root: TreeNode) -> bool:
    #     if not root:
    #         return True
    #     ldepth = self.depth(root.left)
    #     rdepth = self.depth(root.right)
    #     return abs(ldepth - rdepth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    #
    # def depth(self, root: TreeNode):
    #     if not root:
    #         return 0
    #     ldepth = self.depth(root.left)
    #     rdepth = self.depth(root.right)
    #     return max(ldepth, rdepth) + 1

    def dfs(self, root: TreeNode):
        if not root:
            return 0
        ld = self.dfs(root.left)
        if ld == -1:
            return -1
        rd = self.dfs(root.right)
        if rd == -1:
            return -1
        return max(ld, rd) + 1 if abs(ld - rd) <= 1 else -1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.dfs(root) != -1
