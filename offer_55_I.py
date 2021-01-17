# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def maxDepth(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     ld = self.maxDepth(root.left)
    #     rd = self.maxDepth(root.right)
    #     return 1 + max(ld, rd)

    def maxDepth(self, root: TreeNode) -> int:
        from collections import deque

        if not root:
            return 0
        depth, queue = 0, deque([root])
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(Solution().maxDepth(root))