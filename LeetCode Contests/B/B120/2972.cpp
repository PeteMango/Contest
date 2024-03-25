#include <bits/stdc++.h>
using namespace std;

long long countOverlap(vector<int> &a, vector<int> &b)
{
    long long ans = 0;
    int l = 0, r = 0;
    while (l < a.size() && r < b.size())
    {
        if (a[l] < b[r])
        {
            ans += (b.size() - r);
            l++;
        }
        else
        {
            r++;
        }
    }
    return ans;
}

long long incremovableSubarrayCount(vector<int> &nums)
{
    int n = nums.size();
    if (n == 1)
    {
        return 1;
    }

    int l = 0, r = n - 1;
    vector<int> a, b;

    // partition array into two parts
    while (l + 1 < n && nums[l] < nums[l + 1]) // get left ascending array
    {
        a.push_back(nums[l]);
        l++;
    }
    a.push_back(nums[l]);

    while (r - 1 >= 0 && nums[r] > nums[r - 1]) // get right ascending array
    {
        b.push_back(nums[r]);
        r--;
    }
    b.push_back(nums[r]);

    reverse(b.begin(), b.end());

    if (r < l) // entire array is sorted, return all subarrays
    {
        return ((long long)(n * (n + 1)) / 2ll);
    }

    long long ans = a.size() + b.size() + 1 + countOverlap(a, b);
    return ans;
}

int main()
{
    vector<int> v = {1, 2, 3, 4};
    cout << incremovableSubarrayCount(v) << "\n";
}
