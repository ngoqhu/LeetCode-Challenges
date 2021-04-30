class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0

        while i < len(s):
            if s[i] == 'I':
                if i + 1 == len(s):
                    result += 1
                    break

                if s[i + 1] == 'V':
                    result += 4
                    i += 1
                elif s[i + 1] == 'X':
                    result += 9
                    i += 1
                else:
                    result += 1
            elif s[i] == 'V':
                result += 5
            elif s[i] == 'X':
                if i + 1 == len(s):
                    result += 10
                    break

                if s[i + 1] == 'L':
                    result += 40
                    i += 1
                elif s[i + 1] == 'C':
                    result += 90
                    i += 1
                else:
                    result += 10
            elif s[i] == 'L':
                result += 50
            elif s[i] == 'C':
                if i + 1 == len(s):
                    result += 100
                    break

                if s[i + 1] == 'D':
                    result += 400
                    i += 1
                elif s[i + 1] == 'M':
                    result += 900
                    i += 1
                else:
                    result += 100
            elif s[i] == 'D':
                result += 500
            else:
                result += 1000

            i += 1

        return result
