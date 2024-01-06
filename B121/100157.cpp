#include <bits/stdc++.h>
using namespace std;

int missingInteger(vector<int> &nums)
{
    int n = nums.size(), curSum = nums[0];
    for (int i = 1; i < n; i++)
    {
        if (nums[i] == nums[i - 1] + 1)
        {
            curSum += nums[i];
        }
        else
        {
            break;
        }
    }

    unordered_set<int> ust;
    for (auto k : nums)
    {
        ust.emplace(k);
    }

    for (int i = curSum; i < 100000; i++)
    {
        if (ust.find(i) == ust.end())
        {
            return i;
        }
    }

    return -1;
}

int main()
{
    vector<int> v = {1, 2, 3, 9, 2, 10, 8, 3, 10, 2};
    cout << missingInteger(v) << "\n";
}
