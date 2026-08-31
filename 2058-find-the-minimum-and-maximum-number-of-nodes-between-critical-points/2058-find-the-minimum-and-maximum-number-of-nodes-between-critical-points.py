class Solution:
    def nodesBetweenCriticalPoints(self, head):
        # Answer initially
        ans = [-1, -1]

        prev = head
        curr = head.next

        position = 1

        first = -1
        last = -1
        min_distance = float('inf')

        while curr.next is not None:

            next_node = curr.next

            # Check for local maximum or local minimum
            is_max = curr.val > prev.val and curr.val > next_node.val
            is_min = curr.val < prev.val and curr.val < next_node.val

            if is_max or is_min:

                # First critical point
                if first == -1:
                    first = position

                # Calculate distance from previous critical point
                if last != -1:
                    distance = position - last
                    min_distance = min(min_distance, distance)

                # Update latest critical point
                last = position

            prev = curr
            curr = next_node
            position += 1

        # Fewer than 2 critical points
        if first == -1 or first == last:
            return [-1, -1]

        # Maximum distance
        max_distance = last - first

        return [min_distance, max_distance]