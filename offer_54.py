# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root: TreeNode):
        if not root:
            return
        self.dfs(root.right)
        self.k -= 1
        if self.k == 0:
            self.ans = root.val
            return
        self.dfs(root.left)

    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k, self.ans = k, 0
        self.dfs(root)
        return self.ans

