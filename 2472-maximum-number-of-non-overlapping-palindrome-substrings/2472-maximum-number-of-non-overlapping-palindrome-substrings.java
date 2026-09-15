class Solution {
    public int maxPalindromes(String s, int k) {
        int n = s.length();

        // pal[i][j] = true if s[i...j] is a palindrome
        boolean[][] pal = new boolean[n][n];

        // Build palindrome table
        for (int len = 1; len <= n; len++) {
            for (int i = 0; i + len <= n; i++) {
                int j = i + len - 1;

                if (len == 1) {
                    pal[i][j] = true;
                } 
                else if (len == 2) {
                    pal[i][j] = s.charAt(i) == s.charAt(j);
                } 
                else {
                    pal[i][j] = s.charAt(i) == s.charAt(j)
                            && pal[i + 1][j - 1];
                }
            }
        }

        // dp[i] = maximum number of non-overlapping
        // valid palindromes using first i characters
        int[] dp = new int[n + 1];

        for (int j = 0; j < n; j++) {

            // Option 1: don't choose a palindrome ending at j
            dp[j + 1] = dp[j];

            // Option 2: choose a palindrome i...j
            for (int i = 0; i <= j - k + 1; i++) {

                if (pal[i][j]) {
                    dp[j + 1] = Math.max(
                        dp[j + 1],
                        dp[i] + 1
                    );
                }
            }
        }

        return dp[n];
    }
}