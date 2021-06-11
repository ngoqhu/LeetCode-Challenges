class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        reverse(s, 0, len(s) - 1)
    
def reverse(s, l, r):
    if l > r:
        return
    
    s[l], s[r] = s[r], s[l]
    reverse(s, l+1, r-1)
