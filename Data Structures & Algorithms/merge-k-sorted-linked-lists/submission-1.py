# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for head in lists:
            while head:
                arr.append(head.val)
                head = head.next
        arr.sort()
        new_head = ListNode()
        curr = new_head
        for num in arr:
            node = ListNode(num)
            curr.next = node
            curr = curr.next
        return new_head.next
        #WCRT: O(M log M) | Space: O(M) where M is the total number of nodes.
