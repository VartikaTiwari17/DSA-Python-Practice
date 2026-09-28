impl Solution {
    pub fn max_depth(s: String) -> i32 {
        let mut depth = 0;
        let mut max_depth = 0;

        for ch in s.chars() {
            if ch == '(' {
                depth += 1;
                max_depth = max_depth.max(depth);
            } else if ch == ')' {
                depth -= 1;
            }
        }

        max_depth
    }
}