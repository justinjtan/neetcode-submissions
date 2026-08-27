class TrieNode:

    def __init__(self, val: str = None):
        self.val = val
        self.child = [None] * 26
        self.ends_here = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if curr.child[ord(char) - ord('a')]:
                curr = curr.child[ord(char) - ord('a')]
                continue
            node = TrieNode(char)
            curr.child[ord(char) - ord('a')] = node
            curr = node
        curr.ends_here = True
        #WCRT: O(N) | Space: O(1) extra space and O(N) for output list

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if not curr.child[ord(char) - ord('a')]:
                return False
            curr = curr.child[ord(char) - ord('a')]
        if not curr.ends_here:
            return False
        return True
        #WCRT: O(N) | Space: O(1)

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if not curr.child[ord(char) - ord('a')]:
                return False
            curr = curr.child[ord(char) - ord('a')]
        return True
        #WCRT: O(N) | Space: O(1)
        
        