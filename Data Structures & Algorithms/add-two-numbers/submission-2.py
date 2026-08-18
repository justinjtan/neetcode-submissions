# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        has_leftover = False
        res_head = l1
        while curr1 or curr2:
            prev = curr1 or curr2
            if not curr1:
                res_head = l2
            res = has_leftover
            res += curr1.val if curr1 else 0
            res += curr2.val if curr2 else 0
            has_leftover = True if res >= 10 else False
            if curr1:
                curr1.val = res % 10
            if curr2:
                curr2.val = res % 10
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        if has_leftover:
            prev.next = ListNode(1, None)
        return res_head
        #WCRT: O(max(n,m)) | Space: O(1)

