class Solution:
    def trailingZeroes(self, n: int) -> int:
        res, i = 0, 1
        while True:
            div = n // (5 ** i)
            if div == 0:
                return res
            res += div
            i += 1
