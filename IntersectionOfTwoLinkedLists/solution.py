# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        first = headA
        second = headB
        
        if first is None or second is None:
            return None
        
        while first != second:
            first = first.next
            second = second.next
            
            if first == second:
                return first
            
            if first is None:
                first = headB
            
            if second is None:
                second = headA
        
        return first
