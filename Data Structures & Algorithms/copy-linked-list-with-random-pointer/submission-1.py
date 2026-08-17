"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        random_map = {}
        while curr:
            random_map[curr] = Node(curr.val)
            curr = curr.next
        new_head = random_map[head]
        while head:
            if head.next:
                random_map[head].next = random_map[head.next]
            pt = head.random
            if pt:
                random_map[head].random = random_map[pt]
            head = head.next
        return new_head
        #WCRT: O(N) | Space: O(N)