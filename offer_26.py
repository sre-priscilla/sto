from offer_32_III import TreeNode


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recursion(a: TreeNode, b: TreeNode):
            if not b:
                return True
            if not a or a.val != b.val:
                return False
            return recursion(a.left, b.left) and recursion(a.right, b.right)

        if A is None or B is None:
            return False
        if recursion(A, B):
            return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)