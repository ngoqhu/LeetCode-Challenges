class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [None] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            row = [1] * (i + 1)
            mid = (i >> 1) + 1
            for j in range(1, mid):
                value = result[i-1][j-1] + result[i-1][j]
                row[j] = value
                row[len(row)-j-1] = value
            result[i] = row
        return result[i]
