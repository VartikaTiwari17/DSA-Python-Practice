class Solution:
    def shortestBeautifulSubstring(self, s, k):
        ans = ""

        for i in range(len(s)):
            ones = 0

            for j in range(i, len(s)):
                if s[j] == '1':
                    ones += 1

                if ones == k:
                    curr = s[i:j + 1]

                    if ans == "" or len(curr) < len(ans) or (len(curr) == len(ans) and curr < ans):
                        ans = curr

                    break

                if ones > k:
                    break

        return ans