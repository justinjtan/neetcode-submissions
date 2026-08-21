# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        curr = new_head
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        return new_head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        step = 1
        while step <= math.ceil(math.log(len(lists), 2)):
            for idx in range(0, len(lists), pow(2, step)):
                if idx + pow(2, step - 1) < len(lists):
                    lists[idx] = self.mergeList(lists[idx], lists[idx + pow(2, step - 1)])
            step += 1
        return lists[0]
        #WCRT: O(M log N) | Space: O(1) where M is the total number of nodes and N is the length of lists.
        
