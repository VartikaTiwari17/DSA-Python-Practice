class Solution:
    def divide(self, dividend, divisor):

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Special overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Result ka sign
        negative = (dividend < 0) != (divisor < 0)

        # Positive values mein convert
        a = -dividend if dividend < 0 else dividend
        b = -divisor if divisor < 0 else divisor

        quotient = 0

        # Largest possible multiple subtract karo
        while a >= b:
            value = b
            multiple = 1

            while a >= (value << 1):
                value <<= 1
                multiple <<= 1

            a -= value
            quotient += multiple

        # Sign apply karo
        if negative:
            quotient = -quotient

        # 32-bit range
        if quotient > INT_MAX:
            return INT_MAX

        if quotient < INT_MIN:
            return INT_MIN

        return quotient