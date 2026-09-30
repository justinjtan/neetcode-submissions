class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = [p for p in path.split('/') if p and p != '.']
        stack = []
        for d in dirs:
            if d == "..":
                stack.pop() if stack else None
            else:
                stack.append(d)
        return '/' + "/".join(stack)
        #WCRT: O(N) | Space: O(N)