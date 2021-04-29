class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = 0
        idxOfResults = []
        
        for i in range(len(nums)):
            if result == 0:
                result += nums[i]
                idxOfResults.append(i)
            else:
                if result + nums[i] == target:
                    idxOfResults.append(i)
                    return idxOfResults
                else:
                    result = 0
                    idxOfResults.clear()

        return idxOfResults
