class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        start, end = 0, 0
        
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # length of palindrome = right - left - 1
            return left + 1, right - 1
        
        for i in range(len(s)):
            # odd-length palindrome centered at i
            l1, r1 = expandAroundCenter(i, i)
            if r1 - l1 > end - start:
                start, end = l1, r1
            
            # even-length palindrome centered between i and i+1
            l2, r2 = expandAroundCenter(i, i + 1)
            if r2 - l2 > end - start:
                start, end = l2, r2
        
        return s[start:end + 1]