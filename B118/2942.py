from typing import List


def hasCharacter(word: str, c: str) -> bool:
    for x in word:
        if x == c:
            return True

    return False


def findWordsContaining(words: List[str], x: str) -> List[int]:
    indices = []
    for i, str in enumerate(words):
        if hasCharacter(str, x):
            indices.append(i)

    return indices


words = ["abc", "bcd", "aaaa", "cbc"]
x = "a"
print(findWordsContaining(words, x))
