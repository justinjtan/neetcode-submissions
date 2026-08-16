# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def findLenList(self, head: Optional[ListNode]) -> int:
        ct = 0
        while head:
            ct += 1
            head = head.next
        return ct

    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        ct = 1
        list_len = self.findLenList(curr) // 2 + 1
        while curr and ct < list_len:
            curr = curr.next
            ct += 1
        alt_head = curr.next
        curr.next = None
        alt_head = self.reverseList(alt_head)
        prev, curr = head, head.next
        while alt_head and curr:
            prev.next = alt_head
            temp = alt_head.next
            alt_head.next = curr
            prev = curr
            curr = curr.next
            alt_head = temp
        #WCRT: O(N) | Space: O(1)