import heapq

class Solution:
    def busiestServers(self, k, arrival, load):

        # Segment tree: initially all servers are available
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        # Find first available server >= position
        def find(pos):
            if tree[1] == 0:
                return -1

            def search(node, left, right):
                if tree[node] == 0 or right <= pos:
                    return -1

                if right - left == 1:
                    return left

                mid = (left + right) // 2

                result = search(node * 2, left, mid)

                if result != -1:
                    return result

                return search(node * 2 + 1, mid, right)

            return search(1, 0, size)

        # Update server availability
        def update(index, value):
            index += size
            tree[index] = value

            index //= 2

            while index:
                tree[index] = (
                    tree[index * 2] + tree[index * 2 + 1]
                )
                index //= 2

        busy = []
        count = [0] * k

        for i in range(len(arrival)):

            # Release servers whose requests are completed
            while busy and busy[0][0] <= arrival[i]:
                finish, server = heapq.heappop(busy)
                update(server, 1)

            # Find the next available server
            start = i % k

            server = find(start)

            if server == -1:
                server = find(0)

            if server == -1:
                continue

            # Assign request
            count[server] += 1

            update(server, 0)

            finish_time = arrival[i] + load[i]

            heapq.heappush(
                busy,
                (finish_time, server)
            )

        # Find busiest servers
        maximum = max(count)

        return [
            i for i in range(k)
            if count[i] == maximum
        ]