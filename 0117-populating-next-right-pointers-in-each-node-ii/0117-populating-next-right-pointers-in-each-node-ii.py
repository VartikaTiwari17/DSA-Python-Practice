class Solution:
    def connect(self, root):
        if not root:
            return None

        curr = root

        while curr:
            # Dummy node for the next level
            dummy = Node(0)
            tail = dummy

            # Traverse current level using next pointers
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next

                if curr.right:
                    tail.next = curr.right
                    tail = tail.next

                curr = curr.next

            # Move to the first node of next level
            curr = dummy.next

        return root