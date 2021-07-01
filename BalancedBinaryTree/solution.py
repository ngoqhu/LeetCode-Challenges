# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def areSubTreesBalanced(node, height):
            if not node:
                return 0
            
            left = areSubTreesBalanced(node.left, 1 + height)
            right = areSubTreesBalanced(node.right, 1 + height)
            
            if abs(left - right) > 1:
                return float('inf')
            
            return 1 + max(left, right)
        
        return areSubTreesBalanced(root, 0) != float('inf')
