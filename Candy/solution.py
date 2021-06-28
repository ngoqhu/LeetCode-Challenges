class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        
        candies = [1 for k in range(n)]
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in range(n-1, 0, -1):
            if candies[i-1] <= candies[i] and ratings[i-1] > ratings[i]:
                candies[i-1] = candies[i] + 1
        
        return sum(candies)
