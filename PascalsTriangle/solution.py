class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [None] * numRows
        for i in range(numRows):
            row = [1] * (i + 1)
            mid = (i >> 1) + 1
            for j in range(1, mid):
                value = result[i-1][j-1] + result[i-1][j]
                row[j] = value
                row[len(row)-j-1] = value
            result[i] = row
        return result
