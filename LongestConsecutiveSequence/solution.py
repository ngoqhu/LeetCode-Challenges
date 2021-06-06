class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0
        curr_longest = min(1, len(nums))

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue

            if nums[i] - 1 == nums[i - 1]:
                curr_longest += 1
            else:
                longest = max(longest, curr_longest)
                curr_longest = 1		

        return max(longest, curr_longest)
