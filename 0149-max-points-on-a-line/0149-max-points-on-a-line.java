import java.util.*;

class Solution {
    public int maxPoints(int[][] points) {

        int n = points.length;

        if (n <= 2)
            return n;

        int ans = 0;

        for (int i = 0; i < n; i++) {

            HashMap<String, Integer> map = new HashMap<>();

            for (int j = i + 1; j < n; j++) {

                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];

                int g = gcd(dx, dy);

                dx /= g;
                dy /= g;

                // Normalize sign
                if (dx < 0) {
                    dx = -dx;
                    dy = -dy;
                }

                // Vertical line
                if (dx == 0) {
                    dy = 1;
                }

                // Horizontal line
                if (dy == 0) {
                    dx = 1;
                }

                String slope = dy + "/" + dx;

                int count = map.getOrDefault(slope, 0) + 1;
                map.put(slope, count);

                ans = Math.max(ans, count + 1);
            }
        }

        return ans;
    }

    private int gcd(int a, int b) {

        a = Math.abs(a);
        b = Math.abs(b);

        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }

        return a;
    }
}