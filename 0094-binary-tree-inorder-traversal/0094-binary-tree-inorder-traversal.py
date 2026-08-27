class Solution:
    def inorderTraversal(self, root):
        result = []
        stack = []
        current = root

        while current or stack:

            # Go as left as possible
            while current:
                stack.append(current)
                current = current.left

            # Process node
            current = stack.pop()
            result.append(current.val)

            # Move to right subtree
            current = current.right

        return result