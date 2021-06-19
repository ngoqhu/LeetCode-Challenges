    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        sum_of_previous = 0

        for i in range(len(nums)):
            sum_of_previous += nums[i]
            result.append(sum_of_previous)

        return result
