class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        for i in range(len(words) - 1):
            found_diff = False
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    adj[words[i][j]].append(words[i + 1][j])
                    found_diff = True
                    break
            if not found_diff and len(words[i]) > len(words[i + 1]):
                return ""
        res = deque([])
        visited = set()

        def dfs(char):
            if char in visited:
                return ""
            if not adj.get(char, True):
                return True
            visited.add(char)
            for nei in adj.get(char, []):
                curr = dfs(nei)
                if curr == "":
                    return ""
            visited.remove(char)
            adj[char] = False
            res.appendleft(char)
            return True

        unique_chars = set()
        for word in words:
            for char in word:
                unique_chars.add(char)

        for char in list(unique_chars):
            if not dfs(char):
                return ""
        return "".join(list(res))
        #WCRT: O(N + E + V) | Space: O(E + V) where N is the sum of the length of all words in words and E is the number of edges and V is the number of unique characters.