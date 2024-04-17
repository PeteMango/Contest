# FenwickTree (Binary Index Tree Implementation

class FenwickTree:
    def __init__(self, size):
        """
        Initialize the Fenwick Tree with a given size.

        Args:
            size (int): The size of the array for which the tree is constructed.
        """

        self.size = size
        self.tree = [0] * (size + 1)
        self.lazy = [0] * (size + 1)  # Additional tree for range updates

    def update(self, index, delta):
        """
        Increment the value at `index` by `delta` for point update.

        Args:
            index (int): The index in the array to update.
            delta (int): The value to add at the index.
        """

        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def range_update(self, left, right, delta):
        """
        Increment all values in the range [left, right] by `delta`.

        Args:
            left (int): The starting index of the range to update.
            right (int): The ending index of the range to update.
            delta (int): The value to add within the range.
        """

        self._range_update_util(left, delta)
        self._range_update_util(right + 1, -delta)

    def _range_update_util(self, index, delta):
        """
        Helper method to perform range updates using the lazy tree.

        Args:
            index (int): The index to start the update.
            delta (int): The value to add, propagated as needed.
        """

        while index <= self.size:
            self.lazy[index] += delta
            index += index & -index

    def query(self, index):
        """
        Computes the prefix sum of elements up to the `index`.

        Args:
            index (int): The index up to which the sum is computed.

        Returns:
            int: The prefix sum up to the index.
        """

        sum = 0
        original_index = index
        while index > 0:
            sum += self.tree[index]
            index -= index & -index

        index = original_index
        while index > 0:
            sum += self.lazy[index] * (original_index - index + 1)
            index -= index & -index
        return sum

    def range_query(self, left, right):
        """
        Compute sum of region from `left` to `right`.

        Args:
            left (int): Start index of the sub-region.
            right (int): End index of the sub-region.

        Returns:
            int: Sum of the sub-region.
        """

        return self.query(right) - self.query(left - 1)
