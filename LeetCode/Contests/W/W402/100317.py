from typing import List

# segtree template
class SegmentTree:
    def __init__(self, data, func, default):
        self._data = data
        self._func = func
        self._default = default
        self._size = len(data)
        self._tree = [default] * (2 * self._size)
        self._build()

    def _build(self):
        for i in range(self._size):
            self._tree[self._size + i] = self._data[i]
        for i in range(self._size - 1, 0, -1):
            self._tree[i] = self._func(self._tree[i * 2], self._tree[i * 2 + 1])

    def update(self, pos, value):
        pos += self._size
        self._tree[pos] = value
        while pos > 1:
            pos //= 2
            self._tree[pos] = self._func(self._tree[pos * 2], self._tree[pos * 2 + 1])

    def query(self, left, right):
        left += self._size
        right += self._size
        res = self._default
        while left < right:
            if left % 2:
                res = self._func(res, self._tree[left])
                left += 1
            if right % 2:
                right -= 1
                res = self._func(res, self._tree[right])
            left //= 2
            right //= 2
        return res

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def is_peak(nums, i):
            return 0 < i < len(nums) - 1 and nums[i - 1] < nums[i] > nums[i + 1]

        def initial_peaks(nums):
            return [1 if is_peak(nums, i) else 0 for i in range(len(nums))]

        peak_counts = initial_peaks(nums)
        seg_tree = SegmentTree(peak_counts, lambda x, y: x + y, 0)

        results = []

        for query in queries:
            if query[0] == 2:
                _, index, val = query
                nums[index] = val
                for idx in [index - 1, index, index + 1]:
                    if 0 < idx < len(nums) - 1:
                        seg_tree.update(idx, 1 if is_peak(nums, idx) else 0)
            elif query[0] == 1:
                _, li, ri = query
                results.append(seg_tree.query(li + 1, ri))

        return results

s = Solution()

nums = [3,1,4,2,5]
queries = [[2,3,4],[1,0,4]]

nums = [4,1,4,2,1,5]
queries = [[2,2,4],[1,0,2],[1,0,4]]

print(s.countOfPeaks(nums, queries))
