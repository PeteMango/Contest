class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = [-1] * n, [-1] * n

        sk = []
        for i in range(n):
            if i == 0:
                l[i] = 0
                sk.append((heights[i], i))
                continue
            
            while sk and sk[-1][0] >= heights[i]:
                sk.pop()
            
            if not sk:
                l[i] = 0
            else:
                l[i] = sk[-1][1] + 1
            sk.append((heights[i], i))

        sk = []
        for i in range(n-1, -1, -1):
            if i == -1:
                r[i] = n-1
                sk.append((heights[i], i))
                continue
            
            while sk and sk[-1][0] >= heights[i]:
                sk.pop()
            
            if not sk:
                r[i] = n-1
            else:
                r[i] = sk[-1][1] - 1
            sk.append((heights[i], i))

        max_ans = -1
        for i, h in enumerate(heights):
            max_ans = max(max_ans, h * (r[i] - l[i] + 1))

        return max_ans