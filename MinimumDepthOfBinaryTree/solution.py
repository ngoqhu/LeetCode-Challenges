# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        lvl = 0
        queue = deque()
        queue.append(root)
        
        while queue:
            n = len(queue)
            lvl += 1
            
            for i in range(n):
                current = queue.popleft()
                if not current.left and not current.right:
                    return lvl
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
