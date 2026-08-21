class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            # Current line me maximum words find karo
            line = []
            line_len = 0

            while i < len(words):
                # Minimum 1 space between words
                if line_len + len(words[i]) + len(line) > maxWidth:
                    break

                line.append(words[i])
                line_len += len(words[i])
                i += 1

            # Last line OR only one word
            if i == len(words) or len(line) == 1:
                text = " ".join(line)
                text += " " * (maxWidth - len(text))
                result.append(text)
                continue

            # Fully justified line
            total_spaces = maxWidth - line_len
            gaps = len(line) - 1

            space_each = total_spaces // gaps
            extra_spaces = total_spaces % gaps

            text = ""

            for j in range(gaps):
                text += line[j]
                text += " " * (space_each + (1 if j < extra_spaces else 0))

            text += line[-1]

            result.append(text)

        return result