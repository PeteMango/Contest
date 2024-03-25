#include <bits/stdc++.h>
using namespace std;

long long cost(vector<int> &nums, int val)
{
    long long sum = 0;
    for (auto s : nums)
    {
        sum += abs(s - val);
    }
    return sum;
}

long long minimumCost(vector<int> &nums)
{
    sort(nums.begin(), nums.end());
    long long ans = LONG_MAX, median = 0;
    int n = nums.size();
    string tmp = "";

    median = (n % 2) ? nums[n / 2] : (nums[n / 2] + nums[n / 2 - 1]) / 2;

    vector<long long> pos;
    string t = to_string(median);

    pos.push_back(pow(10, t.size() - 1) - 1); // smallest exponential palidrome greater than it
    pos.push_back(pow(10, t.size()) + 1);     // largest exponential palidrome less than it

    for (int i = 0; i < t.size() / 2; ++i) // mirror leftside
    {
        t[t.size() - i - 1] = t[i];
    }
    pos.push_back(stoll(t));

    string t1 = to_string(stoi(t.substr(0, (t.size() + 1) / 2)) + 1); // mirror leftside + 1
    tmp = t1;
    if (t.size() % 2)
    {
        t1 = t1.substr(0, t1.size() - 1);
    }
    reverse(t1.begin(), t1.end());
    pos.push_back(stoll(tmp + t1));

    string t2 = to_string(stoi(t.substr(0, (t.size() + 1) / 2)) - 1); // mirror leftside - 1
    tmp = t2;
    if (t.size() % 2)
    {
        t2 = t2.substr(0, t2.size() - 1);
    }
    reverse(t2.begin(), t2.end());
    pos.push_back(stoll(tmp + t2));

    for (auto possible : pos)
    {
        // cout << possible << "\n";
        ans = min(ans, cost(nums, (int)possible));
    }
    return ans;
}

int main()
{
    vector<int> v = {9, 10, 10};
    cout << minimumCost(v) << "\n";
    cout << "cost is: " << cost(v, 11) << "\n";
}
