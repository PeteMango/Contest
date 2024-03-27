#include <bits/stdc++.h>
using namespace std;

int minimumCost(vector<int> &nums)
{
    if (nums.size() == 3)
    {
        return nums[0] + nums[1] + nums[2];
    }

    int ans = nums[0];
    nums.erase(nums.begin());
    sort(nums.begin(), nums.end());
    return ans + nums[0] + nums[1];
}

int main()
{
    vector<int> v = {1, 2, 3, 12};
    cout << minimumCost(v) << "\n";
}