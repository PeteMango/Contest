def solution(numbers: list[int]):
    num_even = 0

    def is_even(n: int):
        return len(str(n)) % 2 == 0

    for num in numbers:
        if is_even(num):
            num_even += 1

    return num_even
