class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        st = []
        ans = [0] * len(t)
        for i in range(len(t) - 1, -1, -1):
            if not st:
                st.append((t[i], i))
                continue
            
            while st and t[i] >= st[-1][0]:
                st.pop()
            
            if st:
                ans[i] = st[-1][1] - i

            st.append((t[i], i))
        return ans
