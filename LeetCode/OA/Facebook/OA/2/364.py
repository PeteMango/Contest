# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        nums = []
        n = 0

        nums = self.nestedListToList(nestedList)

        mx_depth = self.maxDepth(nums, 1)

        print(f'nums: {nums}\nmx_depth: {mx_depth}')

        return self.getSum(nums, 1, mx_depth)

    def nestedListToList(self, nestedList: List[NestedInteger]) -> List[int]:
        ret = []
        for nested_int in nestedList:
            # print(f'ret is: {ret}')
            if nested_int.isInteger():
                # print(f'got integer: {nested_int.getInteger()}')
                ret.append(nested_int.getInteger())
            else:
                # print(f'got list: {nested_int.getList()}')
                ret.append(self.nestedListToList(nested_int.getList()))
        return ret

    def numElements(self, nestedList) -> int:
        n = 0
        for num in nestedList:
            if type(num) == list:
                n += self.numElements(num)
            else:
                n += 1
        return n

    def maxDepth(self, nestedList, curDepth) -> int:
        mx_depth = curDepth
        if len(nestedList) == 0:
            return 0
        for num in nestedList:
            if type(num) == list:
                mx_depth = max(mx_depth, self.maxDepth(num, curDepth + 1))
            else:
                continue
        return mx_depth

    def getSum(self, nestedList, curDepth, maxDepth) -> int:
        sum = 0
        for num in nestedList:
            if type(num) == list:
                if len(num) == 0:
                    continue
                sum += self.getSum(num, curDepth + 1, maxDepth)
            else:
                sum += (maxDepth - curDepth + 1) * num
        return sum
