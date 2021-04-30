from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])

            if s[i] == ")":
                if stack:               # Check if stack is not empty
                    c = stack.pop()
                    if c != "(":
                        return False
                else:
                    return False

            if s[i] == "]":
                if stack:               # Check if stack is not empty
                    c = stack.pop()
                    if c != "[":
                        return False
                else:
                    return False

            if s[i] == "}":
                if stack:               # Check if stack is not empty
                    c = stack.pop()
                    if c != "{":
                        return False
                else:
                    return False

        if stack:
            return False

        return True
