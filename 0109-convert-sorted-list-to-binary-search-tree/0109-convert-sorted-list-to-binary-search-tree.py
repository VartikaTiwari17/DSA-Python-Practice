class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None

        # Find middle node
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is the middle node
        root = TreeNode(slow.val)

        # Right half
        root.right = self.sortedListToBST(slow.next)

        # Left half
        if prev:
            prev.next = None
            root.left = self.sortedListToBST(head)

        return root
        