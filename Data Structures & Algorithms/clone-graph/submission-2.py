"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        if not node:
            return

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            old_to_new[node] = Node(node.val)
            for neighbor in node.neighbors:
                old_to_new[node].neighbors.append(dfs(neighbor))
            return old_to_new[node]
        
        return dfs(node)
        #WCRT: O(V + E) | Space: O(E)