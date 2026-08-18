class Solution:
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            char = s[right]
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            last_seen[char] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len