class Solution:
    def generateTrees(self, n):
        
        def build(start, end):
            if start > end:
                return [None]

            trees = []

            # Try every number as root
            for root in range(start, end + 1):

                left_trees = build(start, root - 1)
                right_trees = build(root + 1, end)

                # Combine every left tree with every right tree
                for left in left_trees:
                    for right in right_trees:

                        node = TreeNode(root)
                        node.left = left
                        node.right = right

                        trees.append(node)

            return trees

        return build(1, n)