class Solution:
    def isScramble(self, s1, s2):
        memo = {}

        def solve(a, b):
            if a == b:
                return True

            key = (a, b)

            if key in memo:
                return memo[key]

            if sorted(a) != sorted(b):
                memo[key] = False
                return False

            n = len(a)

            for i in range(1, n):

                # No swap
                if solve(a[:i], b[:i]) and solve(a[i:], b[i:]):
                    memo[key] = True
                    return True

                # Swap
                if solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i]):
                    memo[key] = True
                    return True

            memo[key] = False
            return False

        return solve(s1, s2)