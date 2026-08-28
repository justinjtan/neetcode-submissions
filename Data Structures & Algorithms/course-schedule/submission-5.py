class Node:
    
    def __init__(self, val: int, to: List[Node]):
        self.val = val
        self.to = to

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        res = True
        nodes_dict = {}
        for child, parent in prerequisites:
            if parent not in nodes_dict:
                nodes_dict[parent] = Node(parent, [])
            if child not in nodes_dict:
                nodes_dict[child] = Node(child, [])
            nodes_dict[parent].to.append(nodes_dict[child])
        has_visited = set()

        def dfs():
            nonlocal curr, res
            if curr in has_visited:
                if curr in path:
                    res = False
                return
            path.add(curr)
            has_visited.add(curr)
            for target in curr.to:
                temp = curr
                curr = target
                dfs()
                curr = temp
            path.discard(curr)
        
        for node in nodes_dict.values():
            path = set()
            curr = node
            dfs()
        return res
        #WCRT: O(V + E) | Space: O(V)