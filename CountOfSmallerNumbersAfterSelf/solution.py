from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortedList = SortedList()
        ans = []
        
        for num in nums[::-1]:
            idx = SortedList.bisect_left(sortedList, num)
            ans.append(idx)
            sortedList.add(num)
        
        return ans[::-1]
