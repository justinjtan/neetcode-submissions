class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i: [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            prereqs[crs].append(prereq)
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            if prereqs[crs] == []:
                return True
            visited.add(crs)
            for nei in prereqs[crs]:
                if not dfs(nei):
                    return False
            visited.remove(crs)
            prereqs[crs] = []
            return True
        
        for crs in range(numCourses):
            if crs not in visited and not dfs(crs):
                return False
        return True