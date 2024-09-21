class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        for i in range(2**(2*n)):
            # 0 => (
            # 1 => )
            binary = bin(i)[2:]
            while len(binary) < 2*n:
                binary = '0' + binary

            if binary.count('1') != binary.count('0'):
                continue
            
            st = []
            valid = True
            for c in binary:
                if c == '0':
                    st.append(0)
                    continue
                
                if not st:
                    valid = False
                    break
                st.pop()

            if valid:
                ans = ''
                for c in binary:
                    if c == '0':
                        ans += '('
                    else:
                        ans += ')'
            
                ret.append(ans)
        return ret