class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        o = len(s3)
        
        if m == 0:
            return s2 == s3
        elif n == 0:
            return s1 == s3
        elif o == 0:
            return m + n == 0
        elif m + n != o:
            return False
        
        base = [[False] * (n+1) for i in range(m+1)]
        base[0][0] = True
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s3[i-1]:
                    base[i][0] = base[i-1][0]
                
                if s2[j-1] == s3[j-1]:
                    base[0][j] = base[0][j-1]
                
                if s1[i-1] == s3[i+j-1]:
                    base[i][j] = base[i-1][j]
                
                if s2[j-1] == s3[i+j-1]:
                    base[i][j] = base[i][j] or base[i][j-1]
        
        return base[m][n]
