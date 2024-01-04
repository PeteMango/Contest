#include <bits/stdc++.h>
using namespace std;

vector<int> numberGame(vector<int> &nums)
{
    vector<int> arr;
    sort(nums.begin(), nums.end());

    for (int i = 0; i < nums.size(); i += 2)
    {
        arr.push_back(nums[i + 1]);
        arr.push_back(nums[i]);
    }
    return arr;
}

int main()
{
    vector<int> v = {2, 5};
    vector<int> ret = numberGame(v);

    for (int x : ret)
    {
        cout << x << "\n";
    }
}