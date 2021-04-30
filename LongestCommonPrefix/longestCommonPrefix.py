class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]

        for strings in strs:
            result = findCommonSubstring(strings, result)

        return result

def findCommonSubstring(str1: str, str2: str) -> str:
    substring = ""
    i = 0
    j = 0

    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            break

        substring += str1[i]
        i += 1
        j += 1

    return substring
