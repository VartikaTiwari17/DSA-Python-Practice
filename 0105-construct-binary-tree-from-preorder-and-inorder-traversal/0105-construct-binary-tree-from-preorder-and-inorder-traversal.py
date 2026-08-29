class Solution:
    def buildTree(self, preorder, inorder):

        # Store inorder value -> index
        index_map = {}

        for i in range(len(inorder)):
            index_map[inorder[i]] = i

        preorder_index = [0]

        def build(left, right):

            # No nodes
            if left > right:
                return None

            # First element of preorder is root
            root_value = preorder[preorder_index[0]]
            preorder_index[0] += 1

            root = TreeNode(root_value)

            # Find root in inorder
            mid = index_map[root_value]

            # Build left subtree
            root.left = build(left, mid - 1)

            # Build right subtree
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)