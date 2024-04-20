#include <functional>
#include <iostream>
#include <regex>
#include <string>
using namespace std;

class Solution {
public:
    /* helper functions */
    int powmod(int base, int exponent, int modulo) {
        int result = 1;
        while(exponent > 0) {
            if(exponent & 1) {
                result = (result * (unsigned long long)base) % modulo;
            }
            base = (base * (unsigned long long)base) % modulo;
            exponent >>= 1;
        }
        return result;
    }

    int mulmod(int a, int b, int modulo) {
        return ((unsigned long long)a * b) % modulo;
    }

    /* template gcd */
    template <typename T>
    T gcd(T a, T b) {
        while(a != 0) {
            T c = a;
            a = b % a;
            b = c;
        }
        return b;
    }

    /* template co-prime */
    template <typename T>
    bool coPrime(T a, T b) {
        if(((a|b) & 1) == 0) {
            return false;
        }
        return gcd(a, b) == 1;
    }

    /* template lcm */
    template <typename T>
    T lcm(T a, T b) {
        return a * (b / gcd(a, b));
    }

    /* prime sieve from 2-size */
    vector<bool> primeSieve(int size) {
        const int half = (size >> 1)  + 1;
        vector<bool> sieve(half, true);
        sieve[0] = false;

        for(int i = 1; 2*i*i < half; i++) {
            if(sieve[i]) {
                int current = 3*i+1;
                while(current < half) {
                    sieve[current] = false;
                    current += 2*i+1;
                }
            }
        }

        return sieve;
    }

    /* slower but accurate */
    bool wheelFactorization(long long x) {
        if(x == 2 || x == 3 || x == 5) {
            return true;
        }
        if(x % 2 == 0 || x % 3 == 0 || x % 5 == 0) {
            return false;
        }

        const int d[] = {6, 4, 2, 4, 2, 4, 6, 2};
        int pos = 1;
        long long i = 7;

        while(i * i <= x) {
            if(x % i == 0) {
                return false;
            }
            i += d[pos];
            pos = (pos + 1) & 7;
        }
        return x > 1;
    }

    /* faster but probabilitiec primality */
    bool millerRabin(long long x) {
        if(x < 31) {
            const int bitmaskPrimes2to31 = 0x208A28Ac;
            return (bitmaskPrimes2to31 & (1 << x)) != 0;
        }

        if(x == 1 || x == 2) {
            return true;
        }

        if(x % 2 == 0 || x % 3 == 0 || x % 5 == 0 || x % 7 == 0 || x % 11 == 0 || x % 13 == 0 || x % 17 == 0) {
            return false;
        }

        if(x < 17*19) {
            return true;
        }

        const int *r, R1[] = {377687, -1}, R2[] = {31, 73, -1}, R3[] = {2, 7, 61, -1}, R4[] = {2, 13, 23, 1662803, -1}, R5[] = {2, 325, 9375, 28178, 450775, 9780504, 1795265022, -1};

        if(x < 5329) r = R1;
        else if(x < 9080191) r = R2;
        else if(x < 4759123141LL) r = R3;
        else if(x < 1122004669633LL) r = R4;
        else r = R5;

        long long d = x-1;
        d >>= 1;

        int shift = 0;
        while((d & 1) == 0) {
            shift++;
            d >>= 1;
        }

        do {
            int t = powmod(*r++, d, x);
            if(t == 1 || t == x - 1) continue;
            bool maybePrime = false;
            for(int i = 0; i < shift; i++) {
                t = mulmod(t, t, x);
                if(t == 1) return false;
                if(t == x - 1) {
                    maybePrime = true;
                    break;
                }
            }
            if(!maybePrime) return false;
        } while(*r != -1);
        return true;
    }
};

int main() {
    Solution s;
    for(int i = 2; i <= 10000005; i++) {
        if(s.millerRabin(i) != s.wheelFactorization(i)) {
            cout << i << " " << s.millerRabin(i) << " " << s.wheelFactorization(i) << "\n";
        }
    }
}
