class Solution:
    def isSameTree(self, p, q):

        # Both are empty
        if p is None and q is None:
            return True

        # One is empty, other is not
        if p is None or q is None:
            return False

        # Values are different
        if p.val != q.val:
            return False

        # Check left and right subtrees
        return (
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
        )