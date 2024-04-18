#!/bin/python3

from typing import List, Optional
import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

class TrieNode:
    def __init__(self):
        """
        Trie Node:

        Args:
            children (dict): dictionary of childrens
            isEndOfWord (bool): determine if the current node marks the end of word
        """
        self.children = {}
        self.isEndOfWord = 0

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
        node.isEndOfWord += 1

    def search(self, word: str) -> int:
        """
        Searches for a word in the Trie

        Args:
            word (str): the word to search

        Return:
            found (bool): whether the word is in the Trie
        """

        node = self.findEndNode(word)
        return node.isEndOfWord if node else 0

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


def matchingStrings(strings, queries: List[str]):
    t = Trie()

    for word in strings:
        t.insert(word)

    ret = []
    for query in queries:
        ret.append(t.search(query))

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
