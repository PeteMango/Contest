def stock_increase(stocks: list[int]) -> list:
    """Gets the difference and average of the subarray with the maximum difference

    Args:
        stocks (list[int]): list of stock prices

    Raises:
        ValueError: if the stocks is null or empty

    Returns:
        list: [average price of stocks, maximum difference]
    """
    if not stocks:
        raise ValueError('stocks must be a list of numbers')

    max_diff = 0
    cur_len, max_len, start_idx, max_start = 1, 1, 0, 0

    for i in range(1, len(stocks)):
        if stocks[i] >= stocks[i - 1]:  # if increasing still, add to cur
            cur_len += 1
            diff = stocks[i] - stocks[start_idx]
            if diff > max_diff:  # compare cur diff to max diff
                max_diff = diff
                max_len = cur_len
                max_start = start_idx
        else:  # if max increasing subarray breaks
            cur_len, start_idx = 1, i  # reset cur idx and cur length

    final = stocks[max_start:max_start + max_len]  # get final stocks

    return [sum(final) / len(final), final[-1] - final[0]]  # return ans


assert stock_increase([1, 2, 3, 4, 5]) == [3, 4]

assert stock_increase([6, 1, 1, 1, 3, 4, 2]) == [2, 3]

assert stock_increase([0, 1, 0, 3, 4, 9, 0, 2, 3, 4, 5]) == [4, 9]

assert stock_increase([2, 1, 3]) == [2, 2]
