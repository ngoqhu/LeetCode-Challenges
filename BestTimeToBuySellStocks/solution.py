class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        end = len(prices)
        ans = 0

        for i in range(1, end):
            start = min(start, prices[i])
            ans = max(ans, prices[i] - start)

        return ans
