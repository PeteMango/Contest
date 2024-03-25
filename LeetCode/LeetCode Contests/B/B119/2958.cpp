#include <bits/stdc++.h>
using namespace std;

int maxSubarrayLength(vector<int> &nums, int k)
{
    int n = nums.size(), l = 0, r = 0, mx = -1;
    unordered_map<int, int> ump;

    while (l <= r && r < n)
    {
        // this print statement TLE's the problem???
        // cout << l << " " << r << " " << ump[nums[r]] << "\n";
        int x = nums[r]; // number we are dealing with

        if (ump.find(x) == ump.end() || ump[x] == 0) // doesnt exist, so can always insert
        {
            ump.insert_or_assign(x, 1);
            r++;
            continue;
        }
        else
        {
            if (ump[x] + 1 > k) // see if it overflows
            {
                mx = max(mx, r - l);
                for (int i = l; i <= r; i++) // remove all the stuff until you get to one that allows you to go forward
                {
                    l++;
                    ump[nums[i]] -= 1;
                    if (nums[i] == x)
                    {
                        break;
                    }
                }
                ump[x] = k;
                r++;
            }
            else
            {
                ump[x] += 1;
                r++;
            }
        }
    }
    mx = max(mx, r - l);
    return mx;
}

int main()
{
    vector<int> v = {1, 2, 3, 1, 2, 3, 1, 2};
    cout << maxSubarrayLength(v, 2) << "\n";
}