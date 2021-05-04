class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0

        if  (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        coef = 0
        temp = 0    
        for i in range(31, -1, -1):
            if (temp + (divisor << i) <= dividend):
                temp += divisor << i
                coef |= 1 << i
        res = sign * coef

        if not (-2**31 <= res <= 2**31-1):
            return 2**31-1
        else:
            return res
