#include <bits/stdc++.h>
using namespace std;

int incremovableSubarrayCount(vector<int> &nums)
{
    int n = nums.size(), cnt = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 1; j < n - i + 1; j++)
        {
            vector<int> t = nums;
            t.erase(t.begin() + i, t.begin() + i + j);

            if (t.size() == 0 || t.size() == 1)
            {
                cnt++;
                continue;
            }

            bool f = true;

            for (int k = 1; k < t.size(); k++)
            {
                f &= (t[k] > t[k - 1]);
            }

            cnt = f ? cnt + 1 : cnt;
        }
    }
    return cnt;
}

int main()
{
    vector<int> nums = {8, 7, 6, 6};
    cout << incremovableSubarrayCount(nums) << "\n";
}