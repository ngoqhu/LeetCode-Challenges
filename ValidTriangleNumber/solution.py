class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0

        for i in range(2, len(nums)):
            val = nums[i]
            start = 0
            end = i-1
            while start < end:
                if nums[start] + nums[end] > val:
                    ans += (end - start)
                    end -= 1
                else:
                    start += 1

        return ans
