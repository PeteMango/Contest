class Node:
    def __init__(self):
        self.links = [None] * 26
        self.idx = -1
        self.terminal = -1
        self.minimum_length = float('inf')


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word, index):
        word = word[::-1]
        current = self.root
        for char in word:
            char_index = ord(char) - ord('a')
            if not current.links[char_index]:
                current.links[char_index] = Node()
            if len(word) < current.minimum_length:
                current.idx = index
                current.minimum_length = len(word)
            current = current.links[char_index]

        if current.terminal == -1:
            current.terminal = index

    def search(self, word):
        word = word[::-1]
        current = self.root
        for char in word:
            char_index = ord(char) - ord('a')
            if not current.links[char_index]:
                if current.terminal != -1:
                    return current.terminal
                return current.idx
            current = current.links[char_index]

        if current.terminal != -1:
            return current.terminal

        return current.idx


class Solution:
    def stringIndices(self, container, query):
        trie = Trie()
        for i, word in enumerate(container):
            trie.insert(word, i)

        result = [trie.search(word) for word in query]
        return result

s = Solution()

wordsContainer = ["abcd","bcd","xbcd"]
wordsQuery = ["cd","bcd","xyz"]

wordsContainer = ["abcdefgh","poiuygh","ghghgh"]
wordsQuery = ["gh","acbfgh","acbfegh"]

print(s.stringIndices(wordsContainer, wordsQuery))
