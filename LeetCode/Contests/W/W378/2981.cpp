#include <bits/stdc++.h>
using namespace std;

bool containsOneCharacter(string &check)
{
    if (check == "")
    {
        return false;
    }
    for (int i = 0; i < check.length() - 1; i++)
    {
        for (int j = i + 1; j < check.length(); j++)
        {
            if (check[i] != check[j])
            {
                return false;
            }
        }
    }
    return true;
}

int maximumLength(string s)
{
    unordered_set<string> st;
    int n = s.size();

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i + 1; j++)
        {
            string cur = s.substr(i, j);
            if (containsOneCharacter(cur))
            {
                st.emplace(cur);
            }
        }
    }
    st.erase("");

    // for (auto s : st)
    // {
    //     cout << s << "\n";
    // }

    int mx = -1;
    for (string cur : st)
    {
        int cnt = 0;
        for (int i = 0; i < s.length() - cur.length() + 1; i++)
        {
            if (s[i] == cur[0])
            {
                bool f = true;
                for (int j = 0; j < cur.length(); j++)
                {
                    if (s[i + j] != cur[j])
                    {
                        f = false;
                    }
                }
                if (f)
                {
                    cnt++;
                }
            }
        }
        // cout << cur << " " << cnt << "\n";
        if (cnt >= 3)
        {
            mx = max(mx, (int)cur.length());
        }
    }
    return mx;
}

int main()
{
    int ret = maximumLength("cccerrrecdcdccedecdcccddeeeddcdcddedccdceeedccecde");
    cout << ret << "\n";
}