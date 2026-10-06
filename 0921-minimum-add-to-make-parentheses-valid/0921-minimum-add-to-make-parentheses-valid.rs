impl Solution {
    pub fn min_add_to_make_valid(s: String) -> i32 {
        let mut balance = 0;
        let mut ans = 0;

        for ch in s.chars() {
            if ch == '(' {
                balance += 1;
            } else {
                if balance > 0 {
                    balance -= 1;
                } else {
                    ans += 1;
                }
            }
        }

        ans + balance
    }
}