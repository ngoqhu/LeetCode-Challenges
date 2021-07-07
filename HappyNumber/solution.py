class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        res = 0
        
        while res != 1 and res != 4:
            res = 0
            for i in n:
                res += int(i) >> 2
            n = str(res)
        
        if res == 1:
            return True
        else:
            return False
