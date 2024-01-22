#include <bits/stdc++.h>
using namespace std;

int countPartitions(string s, int k)
{
    int numPartitions = 0;
    unordered_set<char> ust;
    for (int i = 0; i < s.length(); i++)
    {
        ust.insert(s[i]);

        if (ust.size() > k)
        {
            numPartitions++;
            ust.clear();
            ust.insert(s[i]);
        }

        // cout << "printing set: ";
        // for (auto m : ust)
        // {
        //     cout << m << " ";
        // }
        // cout << "\n";
    }
    if (!ust.empty())
    {
        numPartitions++;
    }
    return numPartitions;
}

int maxPartitionsAfterOperations(string s, int k)
{
    vector<tuple<char, int, int>> sqz; // char, cnt, before
    char tmp = s[0];
    int cnt = 1, before = 0;
    for (int i = 1; i < s.size(); i++)
    {
        if (s[i] != s[i - 1])
        {
            sqz.push_back({s[i - 1], cnt, before});
            before += cnt;
            tmp = s[i];
            cnt = 1;
        }
        else
        {
            cnt++;
        }
    }
    sqz.push_back({s[s.length() - 1], cnt, before});

    for (int i = 0; i < sqz.size(); i++)
    {
        cout << get<0>(sqz[i]) << " " << get<1>(sqz[i]) << " " << get<2>(sqz[i]) << "\n";
    }

    bool f = false;
    for (int i = 0; i < sqz.size(); i++)
    {
        if (get<1>(sqz[i]) > 1)
        {
            f = true;
        }
    }

    if (f)
    {
        return (sqz.size() + 1) % k == 0 ? (sqz.size() + 1) / k : (sqz.size() + 1 + k) / k;
    }
    return (sqz.size() % k == 0) ? (sqz.size() / k) : ((sqz.size() + k) / k);

    // int mxPartitions = -1;
    // for (int i = 0; i < s.length(); i++)
    // {
    //     char t = s[i];
    //     s[i] = '!';
    //     int partitions = countPartitions(s, k);
    //     if (partitions > mxPartitions)
    //     {
    //         mxPartitions = partitions;
    //     }
    //     s[i] = t;
    // }
    // return mxPartitions;
}

int main()
{
    cout << maxPartitionsAfterOperations("aabaab", 3) << "\n";
}