class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        if len(s) <= 1:
            return True
        
        left = 0
        right = len(s) - 1
        
        while left <= right:
            if not s[left].isalnum():
                left += 1
            if not s[right].isalnum():
                right -= 1
            if (s[left] != s[right]):
                return False
            elif (s[left] == s[right]):
                left += 1
                right -= 1
        return True
