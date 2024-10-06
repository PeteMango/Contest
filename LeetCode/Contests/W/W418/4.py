from bisect import bisect
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        n = max(nums) + 1
        freq = [0] * n
        for num in nums:
            freq[num] += 1

        multiples_count = [0] * n
        for gcd in range(1, n):
            for multiple in range(gcd, n, gcd):
                multiples_count[gcd] += freq[multiple]

        pairs = [0] * n
        for gcd in range(1, n):
            count = multiples_count[gcd]
            pairs[gcd] = count * (count - 1) // 2

        for gcd in range(n-1, 0, -1):
            for multiple in range(2 * gcd, n, gcd):
                pairs[gcd] -= pairs[multiple]

        gcd_count = []
        for gcd in range(1, n):
            if pairs[gcd] > 0:
                gcd_count.append((gcd, pairs[gcd]))

        gcd_values = [gcd for gcd, count in gcd_count]

        psa = []
        for gcd, cnt in gcd_count:
            if len(psa) == 0:
                psa.append(cnt)
                continue
            psa.append(psa[-1]+cnt)

        answer = []
        for query_index in queries:
            idx = bisect(psa, query_index)
            answer.append(gcd_values[idx])

        return answer
