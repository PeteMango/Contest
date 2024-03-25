#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> divideArray(vector<int> &nums, int k)
{
    int n = nums.size() / 3;
    vector<vector<int>> ret;
    sort(nums.begin(), nums.end());

    // cout << "sorted: \n";
    // for (auto x : nums)
    // {
    //     cout << x << " ";
    // }
    // cout << "\n";

    if (nums.size() % 3 != 0)
    {
        vector<vector<int>> newret;
        return newret;
    }

    // for (int i = 1; i < nums.size(); i++)
    // {
    //     if (nums[i] - nums[i - 1] > k)
    //     {
    //         return ret;
    //     }
    // }

    for (int i = 0; i < nums.size(); i += 3)
    {
        int a = nums[i], b = nums[i + 1], c = nums[i + 2];
        ret.push_back({a, b, c});
    }
    for (auto v : ret)
    {
        if (v[1] - v[0] > k || v[2] - v[1] > k || v[2] - v[0] > k)
        {
            vector<vector<int>> newret;
            return newret;
        }
    }

    return ret;
}

int main()
{
    vector<int> nums = {15, 13, 12, 13, 12, 14, 12, 2, 3, 13, 12, 14, 14, 13, 5, 12, 12, 2, 13, 2, 2};
    int k = 2;
    vector<vector<int>> ans = divideArray(nums, k);
    for (auto v : ans)
    {
        for (auto k : v)
        {
            cout << k << " ";
        }
        cout << "\n";
    }
}
