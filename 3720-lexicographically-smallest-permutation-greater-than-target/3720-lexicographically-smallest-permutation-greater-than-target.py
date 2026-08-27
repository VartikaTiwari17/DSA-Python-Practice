class Solution:
    def lexGreaterPermutation(self, s, target):
        n = len(s)

        # Count characters of s
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Find how much of target can be matched as a prefix
        k = 0
        while k < n:
            x = ord(target[k]) - ord('a')

            if cnt[x] == 0:
                break

            cnt[x] -= 1
            k += 1

        # If entire target can be formed,
        # we need to find the next greater permutation.
        if k == n:
            for i in range(n - 1, -1, -1):
                x = ord(target[i]) - ord('a')

                # Put target[i] back into available characters
                cnt[x] += 1

                # Find smallest character greater than target[i]
                for c in range(x + 1, 26):
                    if cnt[c] > 0:
                        ans = target[:i] + chr(c + ord('a'))
                        cnt[c] -= 1

                        for j in range(26):
                            ans += chr(j + ord('a')) * cnt[j]

                        return ans

            return ""

        # target[k] cannot be matched.
        # Try making the string greater exactly at position k.
        x = ord(target[k]) - ord('a')

        for c in range(x + 1, 26):
            if cnt[c] > 0:
                ans = target[:k] + chr(c + ord('a'))
                cnt[c] -= 1

                for j in range(26):
                    ans += chr(j + ord('a')) * cnt[j]

                return ans

        # No greater character at k.
        # Backtrack to an earlier position.
        for i in range(k - 1, -1, -1):
            x = ord(target[i]) - ord('a')

            # Restore target[i]
            cnt[x] += 1

            # Find smallest character greater than target[i]
            for c in range(x + 1, 26):
                if cnt[c] > 0:
                    ans = target[:i] + chr(c + ord('a'))
                    cnt[c] -= 1

                    for j in range(26):
                        ans += chr(j + ord('a')) * cnt[j]

                    return ans

        return ""