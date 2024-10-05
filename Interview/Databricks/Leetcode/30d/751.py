class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        r = n
        def toBin(s: str) -> str:
            parts = s.split('.')
            for i in range(4):
                parts[i] = bin(int(parts[i]))[2:]
                while len(parts[i]) < 8:
                    parts[i] = '0'+parts[i]
            
            return ''.join(parts)

        def lowestBit(ip: str) -> int:
            for i in range(31, -1, -1):
                if ip[i] == '1':
                    return 31-i
            
            return 32

        def addNumber(ip: str, size: int) -> str:
            parts = ip.split('.')
            for i in range(4):
                parts[i] = int(parts[i])
            
            carry = 0
            print(f'part[3]: {parts[3]} size: {size}')
            parts[3] += size
            for i in range(3, -1, -1):
                parts[i] += carry
                carry = parts[i] // 256
                parts[i] %= 256
            
            for i in range(4):
                parts[i] = str(parts[i])
            
            return '.'.join(parts)

        ret = []
        cur = ip
        while r > 0:
            lb = lowestBit(toBin(cur))
            cover_range = 2**(lb)

            while cover_range > r:
                lb -= 1
                cover_range //= 2
            
            ret.append(f'{cur}/{32-lb}')
            r -= cover_range

            cur = addNumber(cur, cover_range)

        return ret
            