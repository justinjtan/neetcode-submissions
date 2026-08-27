class TrieNode:

    def __init__(self):
        self.child = {}
        self.end_of_word = False

class Solution:
    def make_trie(self, words: List[str]) -> TrieNode():
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if curr.child.get(char, None) == None:
                    curr.child[char] = TrieNode()
                curr = curr.child[char]
            curr.end_of_word = True
        return root

    def delete_word(self, root: TrieNode, word: str) -> None:
        curr = root
        char_cutoff = None
        last = None
        for char in word:
            for chx in "abcdefghijklmnopqrstuvwxyz":
                if char != chx and curr.child.get(chx, False):
                    last = curr
                    char_cutoff = char
            curr = curr.child[char]
        if last:
            last.child[char_cutoff] = None

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.make_trie(words)
        has_visited = set()
        ROW, COL = len(board), len(board[0])
        res = set()
        stack = []
        curr = root

        def solve(x, y):
            nonlocal curr
            if res == words:
                return
            if curr.end_of_word:
                word = "".join(stack)
                curr.end_of_word = False
                has_child = False
                for char in "abcdefghijklmnopqrstuvwxyz":
                    if curr.child.get(char, False):
                        has_child = True
                        break
                if not has_child:
                    self.delete_word(root, word)
                res.add(word)
            if x < 0 or y < 0 or x >= COL or y >= ROW or (x, y) in has_visited:
                return
            if curr.child.get(board[y][x]):
                temp = curr
                curr = curr.child[board[y][x]]
                stack.append(board[y][x])
                has_visited.add((x, y))
                solve(x + 1, y)
                solve(x - 1, y)
                solve(x, y + 1)
                solve(x, y - 1)
                has_visited.discard((x, y))
                curr = temp
                stack.pop()

        for y in range(ROW):
            for x in range(COL):
                solve(x, y)
        return list(res)
        #WCRT: O(M * N * 4^W) | Space: O(S) extra space and O(X) for output list where M is row and N is col and W is max(words) S is the total number of characters in words and X is the length of words.