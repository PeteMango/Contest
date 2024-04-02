class Solution:
    def lengthLongestPath(self, input: str) -> int:
        paths = input.split("\n")
        stack = [0]
        max_length = 0

        for path in paths:
            level = path.count("\t")
            name = path.lstrip("\t")

            while len(stack) > level + 1:
                stack.pop()

            if '.' in name:
                max_length = max(max_length, stack[-1] + len(name))
            else:
                stack.append(stack[-1] + len(name) + 1)

        return max_length

s = Solution()

input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"

input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

input = "a"

print(s.lengthLongestPath(input))
