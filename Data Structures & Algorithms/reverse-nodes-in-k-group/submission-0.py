# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
        prev, curr = None, head
        new_head = None
        new_tail = None
        while curr:
            if not prev:
                new_tail = curr
            new_head = curr
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return new_head, new_tail

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ct = 1
        curr = head
        temp_head = head
        prev_tail = None
        res = None
        while curr:
            if ct % k == 0:
                temp = curr.next
                curr.next = None
                new_head, new_tail = self.reverseList(temp_head)
                temp_head = temp
                if not res:
                    res = new_head
                new_tail.next = temp
                if prev_tail:
                    prev_tail.next = new_head
                prev_tail = new_tail
                curr = new_tail
            ct += 1
            curr = curr.next
        return res
        #WCRT: O(N) | Space: O(1)