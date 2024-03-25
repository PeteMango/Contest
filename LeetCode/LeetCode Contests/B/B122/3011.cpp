#include <bits/stdc++.h>
using namespace std;

bool checkBits(int a, int b)
{
    int countA = 0, countB = 0;
    while (a)
    {
        countA += a & 1;
        a >>= 1;
    }

    while (b)
    {
        countB += b & 1;
        b >>= 1;
    }
    return countA == countB;
}

bool canSortArray(vector<int> &nums)
{
    int n = nums.size();
    vector<int> tmp = nums;
    for (int i = 0; i < n - 1; i++)
    {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++)
        {
            if (nums[j] > nums[j + 1])
            {
                if (checkBits(nums[j], nums[j + 1]))
                {
                    int t = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = t;
                }
            }
        }
    }
    sort(tmp.begin(), tmp.end());
    return nums == tmp;
}

int main()
{
    vector<int> v = {8, 4, 2, 30, 15};
    if (canSortArray(v))
    {
        cout << "yes\n";
    }
    else
    {
        cout << "no\n";
    }
}