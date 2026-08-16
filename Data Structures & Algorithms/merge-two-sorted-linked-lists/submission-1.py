# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = ListNode(0, list1), list1
        res_head = prev
        while curr:
            while list2 and list2.val < curr.val:
                temp = list2.next
                list2.next = curr
                prev.next = list2
                prev = prev.next
                list2= temp
            curr = curr.next
            prev = prev.next
        prev.next = list2
        return res_head.next
        #WCRT: O(n+m) | Space: O(1)
