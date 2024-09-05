class Solution:
    def checkTwoChessboards(self, a: str, b: str) -> bool:
        def getColor(coord: str) -> bool:
            # True -> black
            # False -> white

            x, y = ord(coord[0]) - ord('a'), int(coord[1])
            if abs(x-y) % 2 == 0:
                return True
            return False
        
        return getColor(a) == getColor(b)
    
s = Solution()

coordinate1 = "a1"
coordinate2 = "c3"

coordinate1 = "a1"
coordinate2 = "h3"

print(s.checkTwoChessboards(coordinate1, coordinate2))