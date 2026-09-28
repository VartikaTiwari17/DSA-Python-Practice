use std::cell::RefCell;
use std::cmp::max;
use std::rc::Rc;

impl Solution {
    pub fn max_path_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut ans = i32::MIN;

        fn dfs(
            node: Option<Rc<RefCell<TreeNode>>>,
            ans: &mut i32
        ) -> i32 {
            match node {
                None => 0,

                Some(node) => {
                    let node = node.borrow();

                    let left = max(0, dfs(node.left.clone(), ans));
                    let right = max(0, dfs(node.right.clone(), ans));

                    // Path passing through current node
                    *ans = max(*ans, node.val + left + right);

                    // Return one side to parent
                    node.val + max(left, right)
                }
            }
        }

        dfs(root, &mut ans);
        ans
    }
}