class Solution {
private static final long MOD = 1_000_000_007L;


private long[] sum;
private long[] sumSq;
private long[] lazy;
private int n;

public int sumCounts(int[] nums) {
    n = nums.length;

    sum = new long[4 * n];
    sumSq = new long[4 * n];
    lazy = new long[4 * n];

    int[] last = new int[100001];
    java.util.Arrays.fill(last, -1);

    long ans = 0;

    for (int i = 0; i < n; i++) {
        int prev = last[nums[i]];

        update(1, 0, n - 1, prev + 1, i);

        ans = (ans + sumSq[1]) % MOD;

        last[nums[i]] = i;
    }

    return (int) ans;
}

private void apply(int node, int start, int end, long add) {
    long len = end - start + 1L;
    long oldSum = sum[node];

    long increase = (2L * add % MOD * oldSum % MOD
            + len % MOD * add % MOD * add % MOD) % MOD;

    sumSq[node] = (sumSq[node] + increase) % MOD;

    sum[node] = (oldSum + len % MOD * add % MOD) % MOD;

    lazy[node] = (lazy[node] + add) % MOD;
}

private void push(int node, int start, int end) {
    if (lazy[node] == 0 || start == end) {
        return;
    }

    int mid = start + (end - start) / 2;
    long add = lazy[node];

    apply(node * 2, start, mid, add);
    apply(node * 2 + 1, mid + 1, end, add);

    lazy[node] = 0;
}

private void update(int node, int start, int end, int l, int r) {
    if (l > end || r < start || l > r) {
        return;
    }

    if (l <= start && end <= r) {
        apply(node, start, end, 1);
        return;
    }

    push(node, start, end);

    int mid = start + (end - start) / 2;

    update(node * 2, start, mid, l, r);
    update(node * 2 + 1, mid + 1, end, l, r);

    sum[node] = (sum[node * 2] + sum[node * 2 + 1]) % MOD;

    sumSq[node] = (sumSq[node * 2] + sumSq[node * 2 + 1]) % MOD;
}

}
