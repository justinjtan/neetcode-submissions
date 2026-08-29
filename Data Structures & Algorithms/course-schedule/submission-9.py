class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        valid_crs = 0
        while queue:
            crs = queue.popleft()
            valid_crs += 1
            for nei in next_courses[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return valid_crs == numCourses
        #WCRT: O(V + E) | Space: O(V + E)