# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        ans = []
        
        while head:
            ans.append(head.val)
            head = head.next
        
        ans[left-1 : right] = ans[left-1 : right][:: -1]
        head_new = n = ListNode(0)
        
        for i in ans:
            n.next = ListNode(i)
            n = n.next
        
        return head_new.next
        
        
