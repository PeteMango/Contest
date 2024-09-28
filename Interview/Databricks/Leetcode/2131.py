class Solution:
    def longestPalindrome(self, words: List[str]) -> int: 
        d = defaultdict(int)
        matched = 0
        print(sorted(words))
        for w in words:
            if w[::-1] in d and d[w[::-1]] > 0:
                d[w[::-1]] -= 1
                matched += 1
                # print(f'matched at: {w} and {w[::-1]}')
            else:
                d[w] += 1

        print(d)
        single = 0
        for k, v in d.items():
            if k[0] == k[1] and v > 0:
                single += 1
        
        # print(f'matched: {matched}\nsingle: {single}')
        return (2 * matched * 2) + (2 if single >= 1 else 0)