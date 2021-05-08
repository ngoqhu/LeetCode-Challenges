class Solution:
    def jump(self, nums: List[int]) -> int:
        curr = -1
        nxt = 0
        result = 0
        i = 0

        while nxt < len(nums) - 1:
            if i > curr:
                result += 1
                curr = nxt

            nxt = max(nxt, nums[i] + i)
            i += 1

        return result
