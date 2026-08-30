class Solution:

    def word_diff(self, w1: str, w2: str) -> int:
        res = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                res += 1
        return res

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        neighbors = {word: [] for word in wordList}
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if i != j and self.word_diff(wordList[i], wordList[j]) == 1:
                    neighbors[wordList[i]].append(wordList[j])
        initial_queue = []
        
        for word in wordList:
            if self.word_diff(beginWord, word) == 1:
                initial_queue.append(word)
        queue = deque(initial_queue)
        distance = 2
        visited = set()
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return distance
                visited.add(word)
                for nei in neighbors[word]:
                    if nei not in visited:
                        queue.append(nei)
            distance += 1
        return 0