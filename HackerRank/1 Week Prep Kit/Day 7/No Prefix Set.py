#!/bin/python3

from typing import List, Optional
import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertCheck(self, word: str) -> bool:
        node = self.root

        for char in word:
            if node.isEndOfWord:
                return False
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        if node.isEndOfWord:
            return False

        if node.children:
            return False

        node.isEndOfWord = True
        return True

def noPrefix(words: List[str]) -> None:
    t = Trie()

    for word in words:
        if not t.insertCheck(word):
            print('BAD SET')
            print(word)
            return

    print('GOOD SET')

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
