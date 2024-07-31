def solution(message):
    vowels = []
    for i, c in enumerate(message):
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            vowels.append(c)

    if not vowels:
        return message

    c = vowels[-1]
    vowels.insert(0, c)

    ret = ""
    idx = 0
    for i, c in enumerate(message):
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            ret += vowels[idx]
            idx += 1
        else:
            ret += c

    return ret
