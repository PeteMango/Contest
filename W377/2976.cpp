#include <bits/stdc++.h>
using namespace std;

long long minimumCost(string source, string target, vector<char> &original, vector<char> &changed, vector<int> &cost)
{
    int n = original.size(), dp[26][26];

    fill(&dp[0][0], &dp[0][0] + 26 * 26, 0x3f3f3f3f); // c++11 fill

    for (int i = 0; i < n; i++)
    {
        int x = (int)(original[i] - 'a'), y = (int)(changed[i] - 'a');
        dp[x][y] = min(dp[x][y], cost[i]);
    }

    for (int i = 0; i < 26; i++)
    {
        dp[i][i] = 0; // no self -> self cost
    }

    for (int i = 0; i < 26; i++)
    {
        for (int j = 0; j < 26; j++)
        {
            for (int k = 0; k < 26; k++)
            {
                dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k]);
            }
        }
    }

    // for (int i = 0; i < 10; i++)
    // {
    //     for (int j = 0; j < 10; j++)
    //     {
    //         cout << dp[i][j] << " ";
    //     }
    //     cout << "\n";
    // }

    long long ret = 0;
    for (int i = 0; i < source.length(); i++)
    {
        if (source[i] != target[i])
        {
            int x = (int)(source[i] - 'a'), y = (int)(target[i] - 'a');
            if (dp[x][y] == 0x3f3f3f3f) // make sure fill with 0x3f3f3f3f not INT_MAX to avoid overflow
            {
                return -1;
            }
            else
            {
                ret += dp[x][y];
            }
        }
    }
    return ret;
}

int main()
{
    string source = "abadcdadac";
    string target = "baddbccdac";
    vector<char> original = {'b', 'c', 'd', 'c', 'b', 'a'};
    vector<char> changed = {'b', 'b', 'c', 'a', 'd', 'd'};
    vector<int> cost = {8, 5, 9, 1, 10, 2};

    long long ans = minimumCost(source, target, original, changed, cost);
    cout << ans << "\n";
}