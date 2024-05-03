# Fri, May 3, 2024

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [x for x in map(str.strip, version1.split('.')) if x]
        v2 = [x for x in map(str.strip, version2.split('.')) if x]

        print(v1)
        print(v2)

        for num1, num2 in zip(v1, v2):
            if int(num1) < int(num2):
                return -1
            if int(num2) < int(num1):
                return 1


        if len(v1) < len(v2):
            for i in range(len(v1), len(v2)):
                if int(v2[i]) > 0:
                    return -1
        
        if len(v2) < len(v1):
            print('was here')
            for i in range(len(v2), len(v1)):
                if int(v1[i]) > 0:
                    return 1

        return 0
        
s = Solution()

version1 = "1.01"
version2 = "1.001"

version1 = "1.0"
version2 = "1.0.0"

version1 = "0.1"
version2 = "1.1"

print(s.compareVersion(version1, version2))

