class Solution:
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        # Required frequency of each word
        need = {}

        for word in words:
            need[word] = need.get(word, 0) + 1

        result = []

        # Try each possible starting offset
        for offset in range(word_len):

            left = offset
            right = offset
            count = 0
            window = {}

            while right + word_len <= len(s):

                word = s[right:right + word_len]
                right += word_len

                # Word is not required
                if word not in need:
                    window = {}
                    count = 0
                    left = right
                    continue

                # Add word to current window
                window[word] = window.get(word, 0) + 1
                count += 1

                # Too many copies of this word
                while window[word] > need[word]:
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    left += word_len
                    count -= 1

                # All words matched
                if count == word_count:
                    result.append(left)

                    # Move window forward
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    left += word_len
                    count -= 1

        return result