impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut ans = 0;

        for i in 0..32 {
            let mut count = 0;

            for &num in &nums {
                if (num >> i) & 1 == 1 {
                    count += 1;
                }
            }

            if count % 3 != 0 {
                ans |= 1 << i;
            }
        }

        ans
    }
}