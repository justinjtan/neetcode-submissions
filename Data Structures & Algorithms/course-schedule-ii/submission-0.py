class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        next_courses = {i: [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            indegree[crs] += 1
            next_courses[prereq].append(crs)

        initial_queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                initial_queue.append(i)
        
        queue = deque(initial_queue)
        res = []
        while queue:
            crs = queue.popleft()
            res.append(crs)
            for nei in next_courses[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        if len(res) == numCourses:
            return res
        return []
        #WCRT: O(V + E) | Space: O(V + E)