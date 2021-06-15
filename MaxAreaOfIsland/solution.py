class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])
        
        def traverse(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            
            return 1 + traverse(i-1, j) + traverse(i, j-1) + traverse(i+1, j) + traverse(i, j+1)
        
        for i, j in product(range(n), range(m)):
            if grid[i][j] == 1:
                ans = max(ans, traverse(i, j))
        
        return ans
