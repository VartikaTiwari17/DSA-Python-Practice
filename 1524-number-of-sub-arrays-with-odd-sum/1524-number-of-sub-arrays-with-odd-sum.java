class Solution {
    public int numOfSubarrays(int[] arr) {

        int MOD = 1000000007;

        int even = 1;
        int odd = 0;
        int prefix = 0;
        int ans = 0;

        for (int num : arr) {

            prefix += num;

            if (prefix % 2 == 0) {
                ans += odd;
                even++;
            } 
            else {
                ans += even;
                odd++;
            }

            ans %= MOD;
        }

        return ans;
    }
}