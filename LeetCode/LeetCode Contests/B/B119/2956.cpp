#include <bits/stdc++.h>
using namespace std;

vector<int> findIntersectionValues(vector<int> &nums1, vector<int> &nums2)
{
    unordered_set<int> ust1, ust2;
    for (auto k : nums1)
    {
        ust1.insert(k);
    }
    for (auto k : nums2)
    {
        ust2.insert(k);
    }

    int cnt1 = 0, cnt2 = 0;
    for (int i = 0; i < nums1.size(); i++)
    {
        if (ust2.find(nums1[i]) != ust2.end())
        {
            cnt1++;
        }
    }

    for (int i = 0; i < nums2.size(); i++)
    {
        if (ust1.find(nums2[i]) != ust1.end())
        {
            cnt2++;
        }
    }

    vector<int> ret = {cnt1, cnt2};
    return ret;
}

int main()
{
    vector<int> v1 = {4, 3, 2, 3, 1}, v2 = {2, 2, 5, 2, 3, 6};
    cout << findIntersectionValues(v1, v2)[0] << " " << findIntersectionValues(v1, v2)[1] << "\n";
}