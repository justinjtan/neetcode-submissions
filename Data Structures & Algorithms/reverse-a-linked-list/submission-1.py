# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            res = ListNode()
            while head:
                res.val = head.val
                if head.next:
                    temp = res.next
                    res.next = ListNode(res.val, None)
                    res.next.next = temp
                head = head.next
            return res
        #WCRT: O(N) | Space: O(N)