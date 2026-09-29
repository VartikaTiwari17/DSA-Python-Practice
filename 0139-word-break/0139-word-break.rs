use std::collections::HashSet;

impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let n = s.len();

        let dict: HashSet<String> = word_dict.into_iter().collect();

        let mut dp = vec![false; n + 1];

        // Empty string can be segmented
        dp[0] = true;

        for i in 1..=n {
            for j in 0..i {
                if dp[j] && dict.contains(&s[j..i]) {
                    dp[i] = true;
                    break;
                }
            }
        }

        dp[n]
    }
}