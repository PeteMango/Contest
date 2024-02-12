#include <bits/stdc++.h>
using namespace std;

int countMatchingSubarrays(vector<int> &nums, vector<int> &pattern)
{
    int subLen = pattern.size() + 1, cnt = 0;
    for (int i = 0; i <= nums.size() - subLen; i++)
    {
        bool f = true;
        for (int j = 0; j < subLen - 1; j++)
        {
            if (pattern[j] == 1 && nums[i + j] >= nums[i + j + 1])
            {
                f = false;
                break;
            }
            if (pattern[j] == 0 && nums[i + j] != nums[i + j + 1])
            {
                f = false;
                break;
            }
            if (pattern[j] == -1 && nums[i + j] <= nums[i + j + 1])
            {
                f = false;
                break;
            }
        }
        if (f)
        {
            // cout << "idx: " << i << "\n";
            cnt++;
        }
    }
    return cnt;
}

int main()
{
    vector<int> nums = {1, 2, 3, 4, 5, 6}, pattern = {1, 1};
    vector<int> nums2 = {1, 4, 4, 1, 3, 5, 5, 3}, pattern2 = {1, 0, -1};
    cout << countMatchingSubarrays(nums, pattern) << "\n";
}