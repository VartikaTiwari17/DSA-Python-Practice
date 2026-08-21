class Solution:
    def mergeKLists(self, lists):

        import heapq

        heap = []

        # Har linked list ka first node heap mein daalo
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode(0)
        current = dummy

        while heap:
            value, i, node = heapq.heappop(heap)

            # Smallest node ko result mein add karo
            current.next = node
            current = current.next

            # Us list ka next node heap mein daalo
            if node.next:
                heapq.heappush(
                    heap,
                    (node.next.val, i, node.next)
                )

        return dummy.next
        