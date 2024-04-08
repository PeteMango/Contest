# prefix tree / trie

from typing import Optional

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        node = self.getRootNodeForWord(word)
        return node is not None and node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        return self.getRootNodeForWord(prefix) is not None

    def getRootNodeForWord(self, word: str) -> Optional[TrieNode]:
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

# USAGE:
    # t = Trie()

    # t.insert('peter')
    # t.insert('norman')

    # print(t.search('peter'))
    # print(t.startsWith('pet'))
