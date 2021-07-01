class Solution:
    def grayCode(self, n: int) -> List[int]:
        array = []
        array.append(0)
        
        for i in range(1, n+1):
            prevLength = len(array)
            mask = 1 << (i-1)
            for j in range(prevLength, 0, -1):
                array.append(mask + array[j-1])
        
        return array
