# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        fast = slow.next
        slow.next = None
        curr, prev = fast, None
        while curr:
            new_head = curr.next
            curr.next = prev
            prev = curr
            curr = new_head
        
        curr = head
        while prev:
            tmp, tmp2 = curr.next, prev.next
            curr.next = prev
            prev.next = tmp
            prev = tmp2
            curr = tmp