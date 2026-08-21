class Solution:
    def removeNthFromEnd(self, head, n):

        # Dummy node banate hain
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Fast ko n steps aage le jao
        for _ in range(n):
            fast = fast.next

        # Fast aur slow ko saath move karo
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Nth node remove karo
        slow.next = slow.next.next

        return dummy.next