impl Solution {
    pub fn has_valid_path(grid: Vec<Vec<char>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();

        // Path length must be even
        if (m + n - 1) % 2 != 0 {
            return false;
        }

        let max_balance = m + n;

        let mut dp = vec![vec![vec![false; max_balance]; n]; m];

        // Starting cell must be '('
        if grid[0][0] == ')' {
            return false;
        }

        dp[0][0][1] = true;

        for i in 0..m {
            for j in 0..n {
                for balance in 0..max_balance {
                    if !dp[i][j][balance] {
                        continue;
                    }

                    // Move down
                    if i + 1 < m {
                        let new_balance =
                            if grid[i + 1][j] == '(' {
                                balance + 1
                            } else {
                                balance.saturating_sub(1)
                            };

                        if grid[i + 1][j] == '(' || balance > 0 {
                            dp[i + 1][j][new_balance] = true;
                        }
                    }

                    // Move right
                    if j + 1 < n {
                        let new_balance =
                            if grid[i][j + 1] == '(' {
                                balance + 1
                            } else {
                                balance.saturating_sub(1)
                            };

                        if grid[i][j + 1] == '(' || balance > 0 {
                            dp[i][j + 1][new_balance] = true;
                        }
                    }
                }
            }
        }

        dp[m - 1][n - 1][0]
    }
}