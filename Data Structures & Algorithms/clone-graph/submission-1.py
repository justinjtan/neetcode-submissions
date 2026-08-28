"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        curr = node
        node_to_copy = {}
        
        def dfs_create():
            nonlocal curr
            if curr in node_to_copy:
                return
            node_to_copy[curr] = Node(curr.val)
            for neighbor in curr.neighbors:
                temp = curr
                curr = neighbor
                dfs_create()
                curr = temp
        
        dfs_create()    
        curr = node
        seen = set()
        def dfs_connect():
            nonlocal curr
            if curr in seen:
                return
            seen.add(curr)
            for neighbor in curr.neighbors:
                node_to_copy[curr].neighbors.append(node_to_copy[neighbor])
                temp = curr
                curr = neighbor
                dfs_connect()
                curr = temp

        dfs_connect()
        return node_to_copy[node]
        #WCRT: O(V + E) | Space: O(V)