class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_num(s: str):
            try:
                int(s)
                return True
            except:
                return False
        st = []
        for t in tokens:
            if is_num(t):
                st.append(int(t))
                continue

            a, b = st[-2], st[-1]
            st.pop()
            st.pop()

            if t == '+':
                st.append(a+b)
            elif t == '-':
                st.append(a-b)
            elif t == '*':
                st.append(a*b)
            else:
                st.append(int(float(a)/b))
        return int(st[-1])