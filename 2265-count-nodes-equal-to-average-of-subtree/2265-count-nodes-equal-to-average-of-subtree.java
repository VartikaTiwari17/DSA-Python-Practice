class Solution {

    int ans = 0;

    public int averageOfSubtree(TreeNode root) {
        dfs(root);
        return ans;
    }

    // returns {sum, count}
    private int[] dfs(TreeNode node) {

        if (node == null) {
            return new int[]{0, 0};
        }

        // Left subtree
        int[] left = dfs(node.left);

        // Right subtree
        int[] right = dfs(node.right);

        // Total sum of current subtree
        int sum = node.val + left[0] + right[0];

        // Total number of nodes in current subtree
        int count = 1 + left[1] + right[1];

        // Average (integer division automatically rounds down)
        int average = sum / count;

        if (node.val == average) {
            ans++;
        }

        return new int[]{sum, count};
    }
}