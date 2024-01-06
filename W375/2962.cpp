#include <bits/stdc++.h>
using namespace std;

long long countSubarrays(vector<int> &nums, int k)
{
    int mxElement = -1;
    for (auto k : nums)
    {
        if (k > mxElement)
        {
            mxElement = k;
        }
    }

    return 0;
}

int main()
{
    vector<int> v = {4, 2, 1, 9};
    cout << countSubarrays(v, 10) << "\n";
}