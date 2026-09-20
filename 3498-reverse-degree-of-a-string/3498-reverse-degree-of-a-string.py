class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, ch in enumerate(s, 1):
            reverse_value = ord('z') - ord(ch) + 1
            ans += reverse_value * i

        return ans