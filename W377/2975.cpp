#include <bits/stdc++.h>
using namespace std;

int maximizeSquareArea(int m, int n, vector<int> &hFences, vector<int> &vFences)
{
    int MOD = 1e9 + 7;
    long long mx = -1;

    hFences.push_back(1);
    vFences.push_back(1);

    hFences.push_back(m);
    vFences.push_back(n);

    unordered_set<int> hd;
    for (int i = 0; i < hFences.size() - 1; i++)
    {
        for (int j = i + 1; j < hFences.size(); j++)
        {
            hd.emplace(abs(hFences[j] - hFences[i]));
        }
    }

    for (int i = 0; i < vFences.size() - 1; i++)
    {
        for (int j = i + 1; j < vFences.size(); j++)
        {
            if (hd.find(abs(vFences[j] - vFences[i])) != hd.end())
            {
                int vd = vFences[j] - vFences[i];
                long long newMax = vd * 1ll * vd;
                mx = max(mx, newMax);
            }
        }
    }
    return (int)(mx % MOD);
}

int main()
{
    vector<int> hf = {2};
    vector<int> vf = {4};
    int m = 6;
    int n = 7;
    cout << maximizeSquareArea(m, n, hf, vf) << "\n";
}