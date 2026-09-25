class Solution {
    public int candy(int[] ratings) {

        int n = ratings.length;

        int[] left = new int[n];
        int[] right = new int[n];

        // Sabko 1 candy
        for (int i = 0; i < n; i++) {
            left[i] = 1;
            right[i] = 1;
        }

        // Left to Right
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                left[i] = left[i - 1] + 1;
            }
        }

        // Right to Left
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                right[i] = right[i + 1] + 1;
            }
        }

        // Minimum candies
        int total = 0;

        for (int i = 0; i < n; i++) {
            total += Math.max(left[i], right[i]);
        }

        return total;
    }
}