#include <bits/stdc++.h>
using namespace std;

bool hasTrailingZeros(vector<int> &nums)
{
    int cnt = 0;
    for (int i = 0; i < nums.size(); i++)
    {
        if (nums[i] % 2 == 0)
        {
            cnt++;
        }
    }
    if (cnt >= 2)
    {
        return true;
    }
    return false;
}

int main()
{
    vector<int> nums = {1, 3, 5, 7, 9};
    if (hasTrailingZeros(nums))
    {
        cout << "yes\n";
    }
    else
    {
        cout << "no\n";
    }
}