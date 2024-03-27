#include <bits/stdc++.h>
using namespace std;

int maxPalindromesAfterOperations(vector<string> &words)
{
    int freq[26];
    vector<int> sizes;
    for (int i = 0; i < 26; i++)
    {
        freq[i] = 0;
    }

    for (int i = 0; i < words.size(); i++)
    {
        for (int j = 0; j < words[i].size(); j++)
        {
            freq[words[i][j] - 'a']++;
        }
        sizes.push_back(words[i].length());
    }

    int pairs = 0, ans = 0;
    for (int i = 0; i < 26; i++)
    {
        pairs += freq[i] / 2;
    }

    sort(sizes.begin(), sizes.end());
    for (int i = 0; i < sizes.size(); i++)
    {
        pairs -= sizes[i] / 2;
        if (pairs >= 0)
        {
            ans++;
        }
    }
    return ans;
}

int main()
{
    vector<string> words = {"aca", "cc", "acb"};
    cout << maxPalindromesAfterOperations(words) << "\n";
}