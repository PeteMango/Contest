#include <bits/stdc++.h>
using namespace std;

long long calculate(string num, string sfx, int limit)
{
    int n = num.length() - sfx.length();
    if (num.length() < sfx.length())
    {
        return 0;
    }

    if (num.length() == sfx.length())
    {
        return num >= sfx ? 1 : 0;
    }

    string s = num.substr(num.length() - sfx.length(), sfx.length());

    long long ret = 0;

    for (int i = 0; i < n; i++)
    {
        if (limit < (num[i] - '0')) // if the ith digit is over
        {
            ret += (long)powl(limit + 1, n - i);
            return ret;
        }
        ret += (long)(num[i] - '0') * (long)powl(limit + 1, n - 1 - i);
    }
    if (s >= sfx)
    {
        ret++;
    }
    return ret;
}

long long numberOfPowerfulInt(long long start, long long finish, int limit, const string &s)
{
    return calculate(to_string(finish), s, limit) - calculate(to_string(start - 1), s, limit);
}

int main()
{
    cout << numberOfPowerfulInt(1, 32486458654, 4, "1") << endl;
    cout << numberOfPowerfulInt(123546, 32486458654, 4, "1") << endl;
}
