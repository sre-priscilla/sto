# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        from typing import Deque
        from collections import deque

        if root is None:
            return root
        queue: Deque[TreeNode] = deque([root])
        while queue:
            n = len(queue)
            for _ in range(n):
                node: TreeNode = queue.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root