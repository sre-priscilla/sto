# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_p = self.findPath(root, p)
        path_q = self.findPath(root, q)
        i, ancestor = 0, None
        while i < len(path_p) and i < len(path_q):
            if not path_p[i] is path_q[i]:
                break
            else:
                ancestor = path_p[i]
            i += 1
        return ancestor

    def findPath(self, root: TreeNode, target: TreeNode):
        path, curr = [root], root
        while curr.val != target.val:
            if target.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
            path.append(curr)
        return path