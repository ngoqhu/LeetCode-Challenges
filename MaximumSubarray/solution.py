class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        total = 0

        for i in range(len(nums)):
            total += nums[i]

            if total > result:
                result = total

            if total < 0:
                total = 0

        return result
