class Solution:
    mod =  1000000007
    def solve(self,dp,s,i):
        if i == len(s):
            return 1
        if i > len(s):
            return 0
        if dp[i] != -1:
            return dp[i]
        if s[i] == "0":
            dp[i] = 0
            return dp[i]
        one = 0
        if s[i] == '*':
            one += (9*self.solve(dp,s,i+1)) % self.mod
        else:
            one += self.solve(dp,s,i+1)
        
        two = 0
        if  i+1 < len(s):
            if s[i+1] == '*':
                if s[i] == '*':
                    two += (15*self.solve(dp,s,i+2)) % self.mod
                elif s[i] <'2':
                    two += (9*self.solve(dp,s,i+2)) % self.mod
                elif s[i] == '2':
                    two += (6*self.solve(dp,s,i+2)) % self.mod
            else:
                if s[i] == "*" and s[i+1]<'7':
                    two += (2*self.solve(dp,s,i+2))% self.mod
                elif s[i] <'2' or (s[i] == '2' and s[i+1] <'7'):
                    two += self.solve(dp,s,i+2)
        dp[i] = ((one % self.mod + two % self.mod) % self.mod)
        return dp[i]
                
        
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1]*(n+1)
        return self.solve(dp,s,0)
