class Solution:
    def minimumKeypresses(self, s: str) -> int:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        freq.sort(reverse=True)

        req = 0
        idx = 0
        mp = [1] * 9
        for i in range(26):
            req += mp[idx] * freq[i]

            mp[idx] += 1

            idx += 1
            if idx == 9:
                idx = 0

        return req


s = Solution()

str = "apple"

str = "abcdefghijkl"

print(s.minimumKeypresses(str))
