class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends_here = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, s: str) -> None:
        curr = self.root
        for char in s:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.ends_here = True
    
    def find_longest_prefix(self) -> str:
        prefix = []
        curr = self.root
        while len(curr.children) == 1 and not curr.ends_here:
            next_char = next(iter(curr.children))
            prefix.append(next_char)
            curr = curr.children[next_char]
        return "".join(prefix)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for s in strs:
            trie.add_word(s)
        return trie.find_longest_prefix()
        #WCRT: O(N * M) | Space: O(M) where N is length of strs and M is the longest string in strs.