from typing import List

class Solution:
    def __init__(self):
        """
        Initialize constants and base witnesses used in the Miller-Rabin primality tests.
        """
        self.bitmask_primes_2_to_31 = 0x208A28Ac
        self.wheel = [6, 4, 2, 4, 2, 4, 6, 2]
        self.R1 = [377687, -1]
        self.R2 = [31, 73, -1]
        self.R3 = [2, 7, 61, -1]
        self.R4 = [2, 13, 23, 1662803, -1]
        self.R5 = [2, 325, 9375, 28178, 450775, 9780504, 1795265022, -1]

    def powmod(self, base: int, exponent: int, modulo: int) -> int:
        """
        Computes (base^exponent) mod modulo using binary exponentiation.

        Args:
            base (int): The base of the exponentiation.
            exponent (int): The exponent of the exponentiation.
            modulo (int): The modulo for the operation.

        Returns:
            int: The result of (base^exponent) mod modulo.
        """
        result = 1
        while exponent > 0:
            if exponent & 1:
                result = (result * base) % modulo
            base = (base * base) % modulo
            exponent >>= 1
        return result

    def mulmod(self, a: int, b: int, modulo: int) -> int:
        """
        Performs (a * b) mod modulo safely to avoid overflow.

        Args:
            a (int): The first operand.
            b (int): The second operand.
            modulo (int): The modulo for the operation.

        Returns:
            int: The result of (a * b) mod modulo.
        """
        return (a * b) % modulo

    def gcd(self, a: int, b: int) -> int:
        """
        Calculates the Greatest Common Divisor of a and b using Euclid's algorithm.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The GCD of a and b.
        """
        while a != 0:
            a, b = b % a, a
        return b

    def co_prime(self, a: int, b: int) -> bool:
        """
        Checks if two numbers a and b are co-prime, which means their GCD is 1.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            bool: True if a and b are co-prime, False otherwise.
        """
        return self.gcd(a, b) == 1

    def lcm(self, a: int, b: int) -> int:
        """
        Computes the Least Common Multiple of a and b.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The LCM of a and b.
        """
        return a * (b // self.gcd(a, b))

    def wheel_factorization(self, x: int) -> bool:
        """
        Checks if a number is prime using wheel factorization method.

        Args:
            x (int): The number to check for primality.

        Returns:
            bool: True if x is prime, False otherwise.
        """
        if x in [2, 3, 5]:
            return True
        if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
            return False
        pos = 1
        i = 7
        while i * i <= x:
            if x % i == 0:
                return False
            i += self.wheel[pos]
            pos = (pos + 1) & 7
        return x > 1

    def miller_rabin(self, n: int) -> bool:
        """
        Performs the Miller-Rabin probabilistic primality test.

        Args:
            n (int): The number to check for primality.

        Returns:
            bool: True if n is probably prime, False if n is composite.
        """
        if n < 2:
            return False
        if n != 2 and n % 2 == 0:
            return False
        if n < 31:
            return (self.bitmask_primes_2_to_31 & (1 << n)) != 0

        witnesses = self.R5 if n < 1 << 64 else [2]  # For numbers > 2^64, use 2 as a simple witness

        d, r = n - 1, 0
        while d % 2 == 0:
            r += 1
            d //= 2

        for a in witnesses:
            if a == -1:
                break
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True


s = Solution()

for i in range(2, 10 ** 9 + 15):
    if s.wheel_factorization(i) != s.miller_rabin(i):
        print(f'{i} {s.wheel_factorization(i)} {s.miller_rabin(i)}')
