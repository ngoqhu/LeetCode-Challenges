class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return 0
        l = 0
        r = len(nums) - 1
        
        while l < r:
            m = (r+l) // 2  
            if nums[m] > nums[m+1]:
                if nums[m] > nums[m-1]:
                    return m
                else: 
                    r = m
            else:
                l = m + 1
                
        return l
