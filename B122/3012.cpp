#include <bits/stdc++.h>
using namespace std;

int minimumArrayLength(vector<int> &nums)
{
    int n = nums.size(), mn = *min_element(nums.begin(), nums.end()), cnt = 0;
    for (auto k : nums)
    {
        if (k == mn)
        {
            cnt++;
        }
        if (k % mn > 0)
        {
            return 1;
        }
    }

    return (cnt + 1) / 2;
}

int main()
{
    vector<int> v = {2, 3, 4};
    cout << minimumArrayLength(v) << "\n";
}