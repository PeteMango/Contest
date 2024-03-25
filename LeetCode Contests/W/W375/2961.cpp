#include <bits/stdc++.h>
using namespace std;

bool test(int a, int b, int c, int d, int target)
{
    int end = a % 10;
    for (int i = 0; i < b - 1; i++)
    {
        end *= a;
        end %= 10;
    }

    // cout << "end is: " << end << "\n";

    int t = end;
    end %= d;

    // cout << "end here is: " << end << "\n";

    for (int i = 0; i < c - 1; i++)
    {
        end *= t;
        end %= d;
    }

    // cout << "end after is: " << end << "\n";
    return end == target;
}

vector<int> getGoodIndices(vector<vector<int>> &variables, int target)
{
    vector<int> ret;
    int n = variables.size();
    for (int i = 0; i < n; i++)
    {
        if (test(variables[i][0], variables[i][1], variables[i][2], variables[i][3], target))
        {
            ret.push_back(i);
        }
    }
    return ret;
}

int main()
{
    vector<vector<int>> v = {{39, 3, 1000, 1000}};
    int target = 2;
    vector<int> ans = getGoodIndices(v, target);
    for (auto k : ans)
    {
        cout << k << " ";
    }
    cout << "\n";
}