class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = 0
        idxOfResult = []

        for i in range(len(nums)):
            result = nums[i]
            idxOfResult.append(i)

            for j in range(i + 1, len(nums)):
                if result + nums[j] == target:
                    idxOfResult.append(j)
                    return idxOfResult
            
            result = 0
            idxOfResult.clear()
