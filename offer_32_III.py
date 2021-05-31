# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque

        result = []
        if not root:
            return result
        should_reverse, queue = 0, deque([root])
        while queue:
            n, tmp = len(queue), []
            for _ in range(n):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if should_reverse:
                tmp.reverse()
            should_reverse = not should_reverse
            result.append(tmp)
        return result