class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        median = nums[len(nums) // 2]

        for i in range(len(nums)):
            result += abs(nums[i] - median)

        return result
