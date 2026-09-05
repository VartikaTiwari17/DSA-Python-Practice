class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        leftmost = root

        while leftmost.left:
            current = leftmost

            while current:
                current.left.next = current.right

                if current.next:
                    current.right.next = current.next.left

                current = current.next

            leftmost = leftmost.left

        return root