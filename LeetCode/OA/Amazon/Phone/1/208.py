class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndofWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        # insert into tree
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        # mark as end of word
        node.isEndofWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        # still have to check if its the end of word
        return node.isEndofWord


    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
