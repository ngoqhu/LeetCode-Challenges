class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        curr = 0

        if len(nums) == 0:
            return 0

        for i in range(len(nums)):
            if nums[i] != nums[curr]:
                nums[curr + 1], nums[i] = nums[i], nums[curr + 1]
                length += 1
                curr += 1

        return length + 1
