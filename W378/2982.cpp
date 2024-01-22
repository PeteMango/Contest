#include <bits/stdc++.h>
using namespace std;

int maximumLength(string s)
{
    int cnt = 0, mx = -1;
    char prev = s[0];
    unordered_map<char, vector<int>> ump;

    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == prev)
        {
            cnt++;
        }
        else
        {
            ump[prev].push_back(cnt);
            cnt = 1;
            prev = s[i];
        }
    }
    ump[prev].push_back(cnt);

    // for (auto [k, v] : ump)
    // {
    //     cout << k << ": ";
    //     for (auto l : v)
    //     {
    //         cout << l << " ";
    //     }
    //     cout << "\n";
    // }

    for (auto [k, v] : ump)
    {
        sort(v.begin(), v.end());
        if (v.size() == 1)
        {
            mx = max(mx, v[0] - 2);
        }
        else if (v.size() == 2)
        {
            int f = v[1], s = v[0];
            if (f - s >= 2)
            {
                mx = max(mx, f - 2);
            }
            else
            {
                mx = max(mx, f - 1);
            }
        }
        else
        {
            int f = v[v.size() - 1], s = v[v.size() - 2], t = v[v.size() - 3];

            if (f == s && s == t)
            {
                mx = max(mx, f);
            }
            else if (f - s >= 2)
            {
                mx = max(mx, f - 2);
            }
            else
            {
                mx = max(mx, f - 1);
            }
        }
    }
    if (mx == 0)
    {
        mx = -1;
    }
    return mx;
}

int main()
{
    int ret = maximumLength("abcaba");
    cout << ret << "\n";
}