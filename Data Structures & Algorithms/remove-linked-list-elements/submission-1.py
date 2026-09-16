# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return 
        curr, prev = head.next, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
                continue
            prev = curr
            curr = curr.next
        while head and head.val == val:
            head = head.next
        return head