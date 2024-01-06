#include <bits/stdc++.h>
using namespace std;

bool check_limit(int num, int limit)
{
    while (num > 0)
    {
        if (num % 10 > limit)
        {
            return false;
        }
        num /= 10;
    }
    return true;
}

int numberOfPowerfulInt(long long start, long long finish, int limit, const string &s)
{
    int powerful_integers = 0;
    long long suffix = stoll(s);
    int suffix_length = s.length();
    long long base = pow(10, suffix_length);

    if (suffix >= start && suffix <= finish && check_limit(suffix, limit))
    {
        powerful_integers++;
    }

    for (int prefix_length = 1; prefix_length <= 10; prefix_length++)
    {
        long long min_prefix = pow(10, prefix_length - 1);
        long long max_prefix = min(finish / base, (long long)pow(10, prefix_length) - 1);

        if (min_prefix * base + suffix > finish)
        {
            break;
        }

        if (suffix == 0 && prefix_length == 1)
        {
            min_prefix = 1;
        }

        for (long long prefix = min_prefix; prefix <= max_prefix; prefix++)
        {
            if (check_limit(prefix, limit))
            {
                powerful_integers++;
            }
        }
    }

    return powerful_integers;
}

int main()
{
    cout << numberOfPowerfulInt(1, 32486458654, 4, "1") << endl;
    cout << numberOfPowerfulInt(123546, 32486458654, 4, "1") << endl;
}
