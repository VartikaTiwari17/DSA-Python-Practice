class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        # Prefix sums
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # Base case: take all stones
        dp = prefix[-1]

        # Work backwards
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)

        return dp