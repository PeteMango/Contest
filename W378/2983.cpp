#include <bits/stdc++.h>
using namespace std;

vector<bool> canMakePalindromeQueries(string s, vector<vector<int>> &queries)
{
    int n = s.length() / 2, q = queries.size();
    string lhs = s.substr(0, n), rhs = s.substr(n, n);
    reverse(rhs.begin(), rhs.end()); // reverse rhs so compare if lhs = rhs

    vector<int> cmp(n + 5, 0);
    for (int i = 0; i < n; i++)
    {
        cmp[i] = (i ? cmp[i - 1] : 0) + (lhs[i] == rhs[i]); // see which parts is not equal
    }

    vector<bool> ret;

    for (auto &x : queries)
    {
        x[2] = s.length() - 1 - x[2];
        x[3] = s.length() - 1 - x[3];
        swap(x[2], x[3]); // reindex them to fit rhs string
    }

    vector<vector<int>> psaL(n, vector<int>(26, 0)), psaR(n, vector<int>(26, 0)); // psa for lhs and rhs

    for (int i = 0; i < n; i++)
    {
        if (i)
        {
            psaL[i] = psaL[i - 1];
            psaR[i] = psaR[i - 1];
        }
        psaL[i][lhs[i] - 'a']++; // track the chars in these ranges
        psaR[i][rhs[i] - 'a']++;
    }

    // process queries
    for (auto &x : queries)
    {
        // cout << "Start\n";
        int l1 = x[0], r1 = x[1], l2 = x[2], r2 = x[3], l = 0, r = 0; // update indices
        bool f = 1;

        vector<int> f1 = psaL[r1], f2 = psaR[r2];

        for (int i = 0; i < 26; i++) // update the character count in the range
        {
            f1[i] -= (l1 ? psaL[l1 - 1][i] : 0);
            f2[i] -= (l2 ? psaR[l2 - 1][i] : 0);
        }

        // check the characters outside of the interval
        // check from 0 -> min(left)
        l = min(l1, l2) - 1;
        if (l > -1)
        {
            f &= (cmp[l] == l + 1);
            // if (f)
            // {
            //     cout << "true\n";
            // }
            // else
            // {
            //     cout << "false\n";
            // }
        }

        // check from max(right) -> n-1
        l = max(r1, r2) + 1, r = n - 1;
        if (r >= l)
        {
            f &= (cmp[r] - cmp[l - 1] == (r - l + 1));
            // if (f)
            // {
            //     cout << "true\n";
            // }
            // else
            // {
            //     cout << "false\n";
            // }
        }

        // in the middle of both ranges
        if (r1 < l2 or r2 < l1)
        {
            if (r1 < l2)
            {
                l = r1, r = l2;
            }
            else
            {
                l = r2, r = l1;
            }

            if (r - l > 1)
            {
                f &= ((cmp[r - 1] - cmp[l]) == (r - l - 1));
                // if (f)
                // {
                //     cout << "true\n";
                // }
                // else
                // {
                //     cout << "false\n";
                // }
            }
        }

        // check the characters inside of the interval
        // left
        if (l1 <= l2)
        {
            l = l1, r = min(r1, l2 - 1);

            if (r >= l)
            {
                vector<int> fn = psaR[r];
                for (int i = 0; i < 26; i++)
                {
                    fn[i] -= (l > 0 ? psaR[l - 1][i] : 0);
                }

                for (int i = 0; i < 26; i++)
                {
                    f1[i] -= fn[i];
                    f &= (f1[i] >= 0);
                }
            }
        }
        else
        {
            l = l2, r = min(r2, l1 - 1);
            if (r >= l)
            {
                vector<int> fn = psaL[r];
                for (int i = 0; i < 26; i++)
                {
                    fn[i] -= (l > 0 ? psaL[l - 1][i] : 0);
                }

                for (int i = 0; i < 26; i++)
                {
                    f2[i] -= fn[i];
                    f &= (f1[i] >= 0);
                }
            }
        }

        // right
        if (r1 >= r2)
        {
            l = max(l1, r2 + 1), r = r1;
            if (r >= l)
            {
                vector<int> fn = psaR[r];
                for (int i = 0; i < 26; i++)
                {
                    fn[i] -= (l > 0 ? psaR[l - 1][i] : 0);
                }
                for (int i = 0; i < 26; i++)
                {
                    f1[i] -= fn[i];
                    f &= (f1[i] >= 0);
                }
            }
        }
        else
        {
            l = max(l2, r1 + 1), r = r2;
            if (r >= l)
            {
                vector<int> fn = psaL[r];
                for (int i = 0; i < 26; i++)
                {
                    fn[i] -= (l > 0 ? psaL[l - 1][i] : 0);
                }
                for (int i = 0; i < 26; i++)
                {
                    f2[i] -= fn[i];
                    f &= (f2[i] >= 0);
                }
            }
        }

        for (int i = 0; i < 26; i++)
        {
            f &= (f1[i] == f2[i]);
        }

        ret.push_back(f);
    }
    return ret;
}

int main()
{
    string s = "abcabc";
    vector<vector<int>> v = {{1, 1, 3, 5}, {0, 2, 5, 5}};
    auto ret = canMakePalindromeQueries(s, v);
    for (auto p : ret)
    {
        if (p)
        {
            cout << "yes\n";
        }
        else
        {
            cout << "no\n";
        }
    }
}