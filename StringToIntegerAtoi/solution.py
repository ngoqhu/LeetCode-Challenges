class Solution:
    def myAtoi(self, s: str) -> int:
        minus = False
        ans = 0

        s = s.lstrip()	# skipping left whitespaces

        if not s:
            return 0

        if s[0] == "-":
            minus = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        for i in range(len(s)):
            if s[i].isdigit():
                ans = ans * 10 + int(s[i])
            else:
                break

        if minus:
            ans *= -1

        if ans < -pow(2, 31):
            ans = -pow(2, 31)
        elif ans > pow(2, 31) - 1:
            ans = pow(2, 31) - 1

        return ans
