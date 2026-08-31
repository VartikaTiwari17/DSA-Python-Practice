from collections import deque

class Solution:
    def levelOrderBottom(self, root):

        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:

            level = []

            # Number of nodes in current level
            for _ in range(len(queue)):

                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        # Reverse top-to-bottom into bottom-to-top
        result.reverse()

        return result