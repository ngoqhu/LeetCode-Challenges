class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = 0

        for i in range(len(digits)):
            tmp = tmp * 10 + digits[i]

        tmp += 1

        ans = [int(x) for x in str(tmp)]

        return ans
