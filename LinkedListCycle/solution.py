# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        
        while hare.next is not None and hare.next.next is not None:
            turtle = turtle.next
            hare = hare.next.next
            
            if turtle == hare:
                return True
        
        return False
