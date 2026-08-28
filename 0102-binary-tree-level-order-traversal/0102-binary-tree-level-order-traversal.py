from collections import deque

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []

            # Number of nodes in current level
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result