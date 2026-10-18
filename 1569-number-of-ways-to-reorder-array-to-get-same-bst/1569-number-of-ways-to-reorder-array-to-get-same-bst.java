class Solution {
    private static final long MOD = 1_000_000_007L;
    private long[][] combinations;

    public int numOfWays(int[] nums) {
        int n = nums.length;

        // Precompute combinations C(n, r)
        combinations = new long[n + 1][n + 1];

        for (int i = 0; i <= n; i++) {
            combinations[i][0] = 1;
            combinations[i][i] = 1;

            for (int j = 1; j < i; j++) {
                combinations[i][j] =
                    (combinations[i - 1][j - 1]
                    + combinations[i - 1][j]) % MOD;
            }
        }

        long result = solve(nums);

        // Exclude the original ordering
        return (int) ((result - 1 + MOD) % MOD);
    }

    private long solve(java.util.List<Integer> nums) {
        int n = nums.size();

        if (n <= 2) {
            return 1;
        }

        int root = nums.get(0);

        java.util.List<Integer> left = new java.util.ArrayList<>();
        java.util.List<Integer> right = new java.util.ArrayList<>();

        // Divide elements according to BST rules
        for (int i = 1; i < n; i++) {
            if (nums.get(i) < root) {
                left.add(nums.get(i));
            } else {
                right.add(nums.get(i));
            }
        }

        long waysLeft = solve(left);
        long waysRight = solve(right);

        // Interleave left and right subtree elements
        long waysToInterleave =
            combinations[left.size() + right.size()][left.size()];

        return (((waysToInterleave * waysLeft) % MOD)
                * waysRight) % MOD;
    }

    private long solve(int[] nums) {
        java.util.List<Integer> list = new java.util.ArrayList<>();

        for (int num : nums) {
            list.add(num);
        }

        return solve(list);
    }
}