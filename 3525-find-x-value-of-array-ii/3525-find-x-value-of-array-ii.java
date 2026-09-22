class Solution {

    int n, k;
    Node[] tree;

    class Node {
        int prod;
        int[] cnt;

        Node() {
            cnt = new int[k];
        }
    }

    Node merge(Node left, Node right) {

        if (left == null) return right;
        if (right == null) return left;

        Node res = new Node();

        // Complete segment product
        res.prod = (left.prod * right.prod) % k;

        // Prefixes ending in left part
        for (int r = 0; r < k; r++) {
            res.cnt[r] += left.cnt[r];
        }

        // Prefixes which contain all of left + part of right
        for (int r = 0; r < k; r++) {
            int newRem = (left.prod * r) % k;
            res.cnt[newRem] += right.cnt[r];
        }

        return res;
    }

    void build(int idx, int l, int r, int[] nums) {

        if (l == r) {

            tree[idx] = new Node();

            int rem = nums[l] % k;

            tree[idx].prod = rem;
            tree[idx].cnt[rem] = 1;

            return;
        }

        int mid = (l + r) / 2;

        build(idx * 2, l, mid, nums);
        build(idx * 2 + 1, mid + 1, r, nums);

        tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
    }

    void update(int idx, int l, int r, int pos, int value) {

        if (l == r) {

            tree[idx] = new Node();

            int rem = value % k;

            tree[idx].prod = rem;
            tree[idx].cnt[rem] = 1;

            return;
        }

        int mid = (l + r) / 2;

        if (pos <= mid) {
            update(idx * 2, l, mid, pos, value);
        } else {
            update(idx * 2 + 1, mid + 1, r, pos, value);
        }

        tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
    }

    Node query(int idx, int l, int r, int ql, int qr) {

        if (qr < l || r < ql) {
            return null;
        }

        if (ql <= l && r <= qr) {
            return tree[idx];
        }

        int mid = (l + r) / 2;

        Node left = query(idx * 2, l, mid, ql, qr);
        Node right = query(idx * 2 + 1, mid + 1, r, ql, qr);

        return merge(left, right);
    }

    public int[] resultArray(int[] nums, int k, int[][] queries) {

        this.n = nums.length;
        this.k = k;

        tree = new Node[4 * n];

        build(1, 0, n - 1, nums);

        int[] result = new int[queries.length];

        for (int i = 0; i < queries.length; i++) {

            int index = queries[i][0];
            int value = queries[i][1];
            int start = queries[i][2];
            int x = queries[i][3];

            // Update nums[index]
            update(1, 0, n - 1, index, value);

            // Get information for nums[start ... n-1]
            Node res = query(1, 0, n - 1, start, n - 1);

            result[i] = res.cnt[x];
        }

        return result;
    }
}