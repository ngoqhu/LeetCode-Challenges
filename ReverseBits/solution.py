class Solution:
    def reverseBits(self, n: int) -> int:
        left = 0x80000000
        res = 0

        for i in range(32):
            if n & (1 << i) != 0:
                res |= (left >> i) 

        return res
