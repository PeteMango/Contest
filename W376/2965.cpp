#include <bits/stdc++.h>
using namespace std;

vector<int> findMissingAndRepeatedValues(vector<vector<int>> &grid)
{
    int n = grid.size(), a = 0, b = 0;
    unordered_set<int> ust;
    for (int i = 1; i <= n * n; i++)
    {
        ust.emplace(i);
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (ust.find(grid[i][j]) == ust.end())
            {
                a = grid[i][j];
            }
            else
            {
                ust.erase(grid[i][j]);
            }
        }
    }
    for (auto s : ust)
    {
        b = s;
    }
    vector<int> ret = {a, b};
    return ret;
}

int main()
{
    vector<vector<int>> grid = {{9, 1, 7}, {8, 9, 2}, {3, 4, 6}};
    auto ans = findMissingAndRepeatedValues(grid);
    cout << ans[0] << " " << ans[1] << "\n";
}