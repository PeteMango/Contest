#include <bits/stdc++.h>
using namespace std;

int maxFrequencyElements(vector<int> &nums)
{
    vector<int> freq(105, 0);
    for (int i = 0; i < nums.size(); i++)
    {
        freq[nums[i]]++;
    }

    int mxFrequency = 0;
    for (int i = 0; i < 105; i++)
    {
        if (freq[i] > mxFrequency)
        {
            mxFrequency = freq[i];
        }
    }

    int ret = 0;
    for (int i = 0; i < 105; i++)
    {
        if (freq[i] == mxFrequency)
        {
            ret += freq[i];
        }
    }
    return ret;
}

int main()
{
    vector<int> v = {1, 2, 2, 3, 1, 4};
    cout << maxFrequencyElements(v) << "\n";
}