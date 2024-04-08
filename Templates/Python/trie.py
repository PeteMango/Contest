# Prefix Tree (Trie) Implementation

from typing import Optional

class TrieNode:
    def __init__(self):
        """
        Trie Node:

        Args:
            children (dict): dictionary of childrens
            isEndOfWord (bool): determine if the current node marks the end of word
        """
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        """
        Trie:

        Args:
            root (TrieNode): root node of the trie
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie

        Args:
            word (str): word to insert

        Returns:
            None
        """

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        """
        Searches for a word in the Trie

        Args:
            word (str): the word to search

        Return:
            found (bool): whether the word is in the Trie
        """

        node = self.findEndNode(word)
        return node is not None and node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        """
        Checks if any word in the prefix starts with the prefix

        Args:
            prefix (str): the prefix to search for

        Returns:
            found (bool): whether the prefix exists in the trie
        """

        return self.findEndNode(prefix) is not None

    def findEndNode(self, word: str) -> Optional[TrieNode]:
        """
        Returns TrieNode corresponding to the last character of a word

        Args:
            word (str): the word to search for

        Returns:
            endNode (TrieNode): the TrieNode corresponding to the last character
        """

        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def containsSubstr(self, substr: str) -> bool:
        """
        Checks if the trie contains any word that is a substring of the given substr.

        Args:
            substr (str): the substr to search for

        Returns:
            bool: True if any forbidden word is a substring of substr, False otherwise.
        """

        for i in range(len(substr)):
            pCrawl = self.root
            for j in range(i, len(substr)):
                if substr[j] not in pCrawl.children:
                    break
                pCrawl = pCrawl.children[substr[j]]
                if pCrawl.isEndOfWord:
                    return True
        return False
