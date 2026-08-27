class TrieNode:

    def __init__(self):
        self.child = [None] * 26
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            i = ord(char) - ord('a')
            if curr.child[i] == None:
                curr.child[i] = TrieNode()
            curr = curr.child[i]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        res = False
        curr = self.root

        def solve(i):
            nonlocal res, curr
            if i == len(word):
                if curr.end_of_word:
                    res = True
                return
            if word[i] == '.':
                for j in range(26):
                    if curr.child[j]:
                        temp = curr
                        curr = curr.child[j]
                        solve(i + 1)
                        curr = temp
            else:
                child_idx = ord(word[i]) - ord('a')
                if curr.child[child_idx]:
                    temp = curr
                    curr = curr.child[child_idx]
                    solve(i + 1)
                    curr = temp

        solve(0)
        return res
        #WCRT: O()
