# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            leftlen = self.maxDepth(root.left)
            rightlen = self.maxDepth(root.right)
            return max(leftlen, rightlen) + 1
