import java.util.*;

class Solution {

    public int[] maximumWeight(List<List<Integer>> intervals) {

        int n = intervals.size();

        // left, right, weight, original index
        int[][] a = new int[n][4];

        for (int i = 0; i < n; i++) {
            a[i][0] = intervals.get(i).get(0);
            a[i][1] = intervals.get(i).get(1);
            a[i][2] = intervals.get(i).get(2);
            a[i][3] = i;
        }

        // Sort by left endpoint
        Arrays.sort(a, (x, y) -> {
            if (x[0] != y[0]) {
                return Integer.compare(x[0], y[0]);
            }
            return Integer.compare(x[3], y[3]);
        });

        int[] starts = new int[n];

        for (int i = 0; i < n; i++) {
            starts[i] = a[i][0];
        }

        // next[i] = first interval with start > a[i].right
        int[] next = new int[n];

        for (int i = 0; i < n; i++) {
            next[i] = upperBound(starts, a[i][1]);
        }

        long[][] dp = new long[n + 1][5];

        List<Integer>[][] best = new ArrayList[n + 1][5];

        // IMPORTANT: initialize k = 0 for every state
        for (int i = 0; i <= n; i++) {
            for (int k = 0; k <= 4; k++) {
                best[i][k] = new ArrayList<>();
            }
        }

        for (int i = n - 1; i >= 0; i--) {

            for (int k = 1; k <= 4; k++) {

                // Option 1: Skip current interval
                long skipScore = dp[i + 1][k];
                List<Integer> skipList = best[i + 1][k];

                // Option 2: Take current interval
                long takeScore =
                    a[i][2] + dp[next[i]][k - 1];

                List<Integer> takeList =
                    new ArrayList<>(best[next[i]][k - 1]);

                takeList.add(a[i][3]);

                // Keep indices sorted
                Collections.sort(takeList);

                if (takeScore > skipScore) {

                    dp[i][k] = takeScore;
                    best[i][k] = takeList;

                } else if (takeScore < skipScore) {

                    dp[i][k] = skipScore;
                    best[i][k] = new ArrayList<>(skipList);

                } else {

                    // Same score:
                    // choose lexicographically smaller indices
                    if (isSmaller(takeList, skipList)) {
                        dp[i][k] = takeScore;
                        best[i][k] = takeList;
                    } else {
                        dp[i][k] = skipScore;
                        best[i][k] = new ArrayList<>(skipList);
                    }
                }
            }
        }

        List<Integer> ans = best[0][4];

        int[] result = new int[ans.size()];

        for (int i = 0; i < ans.size(); i++) {
            result[i] = ans.get(i);
        }

        return result;
    }

    // First position where arr[pos] > target
    private int upperBound(int[] arr, int target) {

        int left = 0;
        int right = arr.length;

        while (left < right) {

            int mid = left + (right - left) / 2;

            if (arr[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }

    // Lexicographical comparison
    private boolean isSmaller(
        List<Integer> a,
        List<Integer> b
    ) {

        int len = Math.min(a.size(), b.size());

        for (int i = 0; i < len; i++) {

            if (!a.get(i).equals(b.get(i))) {
                return a.get(i) < b.get(i);
            }
        }

        return a.size() < b.size();
    }
}