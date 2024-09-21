class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        for c in s:
            if c == '(' or c == '[' or c == '{':
                st.append(c)
                continue
            
            if not st:
                return False
            
            if c == ')' and st[-1] != '(':
                return False
            if c == ']' and st[-1] != '[':
                return False
            if c == '}' and st[-1] != '{':
                return False
            
            st.pop()

        return len(st) == 0