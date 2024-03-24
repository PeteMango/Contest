from typing import List

class TrieNode:
    def __init__(self, char=''):
        self.char = char
        self.children = []
        self.is_end_of_word = False
        self.word_index = -1  # Stores the index of the word in wordsContainer

    def add(self, word: str, word_index: int):
        node = self
        for char in word:
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node
        node.is_end_of_word = True
        node.word_index = word_index

    def query(self, word: str) -> int:
        node = self
        for char in word:
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                return -1  # Not found in any child
        if node.is_end_of_word:
            return node.word_index  # Exact match found
        else:
            # If not an exact match, find the first word that completes the suffix
            node = self._find_deepest_end(node)
            return node.word_index if node else -1

    def _find_deepest_end(self, node):
        if node.is_end_of_word:
            return node
        for child in sorted(node.children, key=lambda x: x.word_index):
            result = self._find_deepest_end(child)
            if result:
                return result
        return None

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        shortest_len = int(1e6 + 5)
        for word in wordsContainer:
            shortest_len = min(shortest_len, len(word))

        wordsContainerReversed = {word[::-1]: i for i, word in enumerate(wordsContainer)}
        root = TrieNode()
        for word, original_index in wordsContainerReversed.items():
            root.add(word, original_index)

        roots = [TrieNode(char) for char in 'abcdefghijklmnopqrstuvwxyz']
        for word, original_index in wordsContainerReversed.items():
            roots[ord(word[0]) - ord('a')].add(word, original_index)
