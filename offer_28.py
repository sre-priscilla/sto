# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def isSymmetric(self, root: TreeNode) -> bool:
    #
    #     def check(p: TreeNode, q: TreeNode):
    #         if p is None and q is None:
    #             return True
    #         if p is None or q is None:
    #             return False
    #         return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)
    #
    #     return check(root, root)

    def isSymmetric(self, root: TreeNode) -> bool:
        from collections import deque

        queue = deque([root, root])
        while queue:
            p, q = queue.popleft(), queue.popleft()
            if p is None and q is None:
                continue
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            queue.append(p.left)
            queue.append(q.right)
            queue.append(p.right)
            queue.append(q.left)
        return True
