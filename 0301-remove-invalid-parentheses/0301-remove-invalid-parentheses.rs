use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn remove_invalid_parentheses(s: String) -> Vec<String> {
        let mut queue = VecDeque::new();
        let mut visited = HashSet::new();
        let mut result = Vec::new();

        queue.push_back(s.clone());
        visited.insert(s);

        let mut found = false;

        while let Some(current) = queue.pop_front() {
            if Self::is_valid(&current) {
                result.push(current.clone());
                found = true;
            }

            if found {
                continue;
            }

            for i in 0..current.len() {
                let ch = current.as_bytes()[i];

                // Only remove parentheses
                if ch != b'(' && ch != b')' {
                    continue;
                }

                let mut next = current.clone();
                next.remove(i);

                if visited.insert(next.clone()) {
                    queue.push_back(next);
                }
            }
        }

        result
    }

    fn is_valid(s: &str) -> bool {
        let mut balance = 0;

        for ch in s.chars() {
            if ch == '(' {
                balance += 1;
            } else if ch == ')' {
                balance -= 1;

                if balance < 0 {
                    return false;
                }
            }
        }

        balance == 0
    }
}