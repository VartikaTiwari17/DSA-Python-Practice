class Solution:
    def isNumber(self, s):
        i = 0
        n = len(s)

        # Optional sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            i += 1

        # Digits before/after decimal
        digit = False

        while i < n and s[i].isdigit():
            digit = True
            i += 1

        # Decimal part
        if i < n and s[i] == '.':
            i += 1

            while i < n and s[i].isdigit():
                digit = True
                i += 1

        # There must be at least one digit
        if not digit:
            return False

        # Exponent
        if i < n and (s[i] == 'e' or s[i] == 'E'):
            i += 1

            # Optional exponent sign
            if i < n and (s[i] == '+' or s[i] == '-'):
                i += 1

            # Exponent must contain digits
            exp_digit = False

            while i < n and s[i].isdigit():
                exp_digit = True
                i += 1

            if not exp_digit:
                return False

        return i == n