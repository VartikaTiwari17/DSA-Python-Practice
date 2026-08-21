class Solution:
    def isMatch(self, s, p):
        i = 0
        j = 0

        star = -1
        match = 0

        while i < len(s):

            # Normal character or '?'
            if j < len(p) and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1

            # '*' found
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            # Mismatch, but previous '*' exists
            elif star != -1:
                j = star + 1
                match += 1
                i = match

            else:
                return False

        # Remaining pattern must contain only '*'
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)