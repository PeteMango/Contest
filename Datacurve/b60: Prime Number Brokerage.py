import math


def prime_brokerage(numbers: list[int]) -> int:
    if not numbers:
        raise ValueError('numbers must be a list of numbers')

    n = len(numbers)  # get lenght of numbers
    # define prefix sum & product arrays
    prefix_sum, prefix_product = [0] * n, [1] * n

    for idx, num in enumerate(numbers):
        prefix_sum[idx] = num if idx == 0 else num + \
            prefix_sum[idx-1]  # build prefix sum array

        prefix_product[idx] = num if idx == 0 else num * \
            prefix_product[idx-1]  # build prefix product array

    def is_prime(n: int) -> bool:
        if n <= 1:  # base case
            return False

        # check all numbers up to square root of n
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:  # if any of them are divisble return false
                return False

        return True  # if no factors were found, return true

    mx_prime = -1
    for i in range(n):
        lhs = prefix_sum[i]  # get lhs value
        rhs = prefix_product[-1] // prefix_product[i]  # get rhs value
        if lhs > rhs and lhs % rhs == 0 and is_prime(lhs // rhs):
            mx_prime = lhs // rhs  # if lhs // rhs is divisible and prime
        elif rhs > lhs and rhs % lhs == 0 and is_prime(rhs // lhs):
            mx_prime = rhs // lhs  # if rhs // lhs is divisible and prime

    return mx_prime  # return max prime we found


assert prime_brokerage([1, 2, 3, 4, 5]) == 2

assert prime_brokerage([8, 4, 3, 5]) == 3

assert prime_brokerage([3, 6, 4, 2]) == -1

assert prime_brokerage([3, 3, 3, 3]) == 3
\
assert prime_brokerage([3, 0, 3, 3]) == 3
