import java.util.*;

class Solution {
public int maxSum(List<Integer> nums, int k) {
int MOD = 1_000_000_007;
long ans = 0;
int[] bits = new int[31];


    // Count set bits at each position
    for (int num : nums) {
        for (int i = 0; i < 31; i++) {
            if ((num & (1 << i)) != 0) {
                bits[i]++;
            }
        }
    }

    // Construct the maximum possible numbers
    for (int j = 0; j < k; j++) {
        long num = 0;

        for (int i = 0; i < 31; i++) {
            if (bits[i] > 0) {
                num |= (1L << i);
                bits[i]--;
            }
        }

        ans = (ans + num * num) % MOD;
    }

    return (int) ans;
}

}
