class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        cipher = []
        dictionary = defaultdict()

        def translate(c):
            if c not in dictionary:
                dictionary[c] = chr(97 + len(dictionary))
            return dictionary[c]

        def compare(word):
            dictionary.clear()
            for i in range(len(word)):
                if translate(word[i]) != cipher[i]:
                    return
            ans.append(word)

        for c in pattern:
            cipher.append(translate(c))

        for word in words:
            compare(word)

        return ans
