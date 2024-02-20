def lastNonEmptyString(s: str) -> str:
    alph = [0] * 26

    for c in s:
        alph[ord(c) - ord('a')] += 1

    mxFreq = 0

    for i in range(26):
        mxFreq = max(mxFreq, alph[i])

    mxFreq -= 1

    print(f'mxFreq is {mxFreq}')

    t = ""
    for c in s:
        t += c

    rm = [mxFreq] * 26

    ret = ""
    for i in range(len(s)):
        if rm[ord(s[i]) - ord('a')] >= 1:
            rm[ord(s[i]) - ord('a')] -= 1
            continue
        else:
            ret += s[i]

    if len(ret) == 0:
        return t

    return ret


s = "aabcbbca"
print(lastNonEmptyString(s))
