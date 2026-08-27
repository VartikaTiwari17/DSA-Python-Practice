class Solution:
    def restoreIpAddresses(self, s):
        result = []

        def backtrack(start, parts):
            # 4 parts ban gaye
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return

            # Har part ki length 1, 2, ya 3 ho sakti hai
            for length in range(1, 4):

                if start + length > len(s):
                    break

                part = s[start:start + length]

                # Leading zero
                if len(part) > 1 and part[0] == '0':
                    continue

                # Value 0-255 honi chahiye
                if int(part) > 255:
                    continue

                parts.append(part)
                backtrack(start + length, parts)
                parts.pop()

        backtrack(0, [])

        return result
        