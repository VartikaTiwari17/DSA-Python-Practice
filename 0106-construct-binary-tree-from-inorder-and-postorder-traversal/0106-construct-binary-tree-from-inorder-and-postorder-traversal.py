class Solution:
    def buildTree(self, inorder, postorder):

        # Inorder value -> index
        index_map = {}

        for i in range(len(inorder)):
            index_map[inorder[i]] = i

        # Use list so nested function can modify it
        post_index = [len(postorder) - 1]

        def build(left, right):

            if left > right:
                return None

            # Get root from postorder
            root_value = postorder[post_index[0]]
            post_index[0] -= 1

            root = TreeNode(root_value)

            # Find root in inorder
            mid = index_map[root_value]

            # Build RIGHT first
            root.right = build(mid + 1, right)

            # Then LEFT
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)