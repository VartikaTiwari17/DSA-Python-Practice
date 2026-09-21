class Solution {
    public long[] resultArray(int[] nums, int k) {

        long[] ans = new long[k];
        long[] prev = new long[k];

        for (int num : nums) {

            int val = num % k;

            long[] cur = new long[k];

            // Start a new subarray
            cur[val]++;

            // Extend previous subarrays
            for (int r = 0; r < k; r++) {

                int newRemainder = (r * val) % k;

                cur[newRemainder] += prev[r];
            }

            // Add current subarrays to answer
            for (int r = 0; r < k; r++) {
                ans[r] += cur[r];
            }

            prev = cur;
        }

        return ans;
    }
}