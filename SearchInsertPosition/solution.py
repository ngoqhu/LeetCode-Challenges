class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] > target:
            return 0

        if nums[len(nums) - 1] < target:
            return len(nums)

        for i in range(len(nums)):
            if nums[i] == target:
                return i

            if i + 1 != len(nums):
                if nums[i] < target and nums[i + 1] > target:
                    return i + 1
