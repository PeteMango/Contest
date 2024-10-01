class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
    
    def find_longest(self, word: str) -> None:
        node = self.root
        for i, c in enumerate(word):
            if c not in node.children:
                return i
            node = node.children[c]
        
        return len(word)

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        t = Trie()
        for w in arr1:
            t.add(str(w))
        
        max_len = 0
        for w in arr2:
            max_len = max(max_len, t.find_longest(str(w)))
        
        return max_len
        