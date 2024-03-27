#include <bits/stdc++.h>
using namespace std;

int maximumSetSize(vector<int> &nums1, vector<int> &nums2)
{
    int n = nums1.size(), sz = n / 2;
    unordered_set<int> n1, n2, ret;
    for (auto k : nums1)
    {
        n1.insert(k);
    }
    for (auto k : nums2)
    {
        n2.insert(k);
    }

    int duplicates = 0;
    for (auto k : n1)
    {
        if (n2.find(k) != n2.end()) // duplicate in both sets
        {
            duplicates++;
        }
    }

    int u1 = n1.size(), u2 = n2.size();
    if (u1 >= u2)
    {
        u1 = min(u1 - duplicates, sz);
    }
    else if (u2 > u1)
    {
        u2 = min(u2 - duplicates, sz);
    }

    cout << u1 << " " << u2 << " " << duplicates << "\n";

    return min(2 * sz, u1 + u2);
}

int main()
{
    vector<int> v1 = {1, 2, 3, 4}, v2 = {3, 4, 5, 6};
    cout << maximumSetSize(v1, v2) << "\n";
}