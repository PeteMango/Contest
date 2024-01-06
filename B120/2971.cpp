#include <bits/stdc++.h>
using namespace std;

long long largestPerimeter(vector<int> &nums)
{
    int n = nums.size();
    sort(nums.begin(), nums.end());

    long long sum = 0;
    for (int k : nums)
    {
        sum += k;
    }

    for (int i = nums.size() - 1; i >= 0; i--)
    {
        if (sum - nums[i] <= nums[i])
        {
            sum -= nums[i];
            nums.pop_back();
        }
    }
    if (nums.size() < 3)
    {
        return -1;
    }
    return sum;
}

int main()
{
    vector<int> v = {5, 5, 50};
    cout << largestPerimeter(v) << "\n";
}