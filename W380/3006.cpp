#include <bits/stdc++.h>
using namespace std;

vector<int> beautifulIndices(string s, string a, string b, int k)
{
    vector<int> aIndex, bIndex;

    if (a.length() <= s.length())
    {
        for (int i = 0; i < s.length() - a.length() + 1; i++)
        {
            if (s[i] == a[0])
            {
                bool isEqual = true;
                for (int j = 0; j < a.length(); j++)
                {
                    if (s[i + j] != a[j])
                    {
                        isEqual = false;
                        break;
                    }
                }
                if (isEqual)
                {
                    aIndex.push_back(i);
                }
            }
        }
    }

    if (b.length() <= s.length())
    {
        for (int i = 0; i < s.length() - b.length() + 1; i++)
        {
            if (s[i] == b[0])
            {
                bool isEqual = true;
                for (int j = 0; j < b.length(); j++)
                {
                    if (s[i + j] != b[j])
                    {
                        isEqual = false;
                        break;
                    }
                }
                if (isEqual)
                {
                    bIndex.push_back(i);
                }
            }
        }
    }

    //     cout << "AINDEX: \n";
    //     for (auto k : aIndex)
    //     {
    //         cout << k << " ";
    //     }
    //     cout << "\n";

    //     cout << "BINDEX: \n";
    //     for (auto k : bIndex)
    //     {
    //         cout << k << " ";
    //     }
    //     cout << "\n";

    vector<int> ret;
    for (int i = 0; i < aIndex.size(); i++)
    {
        bool isGood = false;
        for (int j = 0; j < bIndex.size(); j++)
        {
            if (abs(aIndex[i] - bIndex[j]) <= k)
            {
                isGood = true;
                break;
            }
        }
        if (isGood)
        {
            ret.push_back(aIndex[i]);
        }
    }
    return ret;

    return aIndex;
}

int main()
{
    string s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel";
    int k = 15;
    vector<int> ans = beautifulIndices(s, a, b, k);
    for (auto k : ans)
    {
        cout << k << " ";
    }
    cout << "\n";
}