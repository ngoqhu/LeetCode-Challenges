class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digits = list(str(x))

        for i in range(len(digits) // 2):
            if digits[i] != digits[len(digits) - 1 - i]:
                return False

        return True
