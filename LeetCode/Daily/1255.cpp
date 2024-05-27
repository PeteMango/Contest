/* Thu, May 23, 2024 */

#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int maxScoreWords(vector<string> &words, vector<char> &letters, vector<int> &score)
    {
        int n = words.size();
        vector<int> freq(26, 0);
        for (int i = 0; i < letters.size(); i++)
        {
            freq[letters[i] - 'a']++;
        }
        set<vector<string>> posCombinations;

        function<void()> getCombinations = [&]()
        {
            for (int i = 0; i < (1 << n); i++)
            {
                vector<string> t;
                for (int j = 0; j < n; j++)
                {
                    if ((i & (1 << j)) != 0)
                    {
                        t.push_back(words[j]);
                    }
                }
                posCombinations.insert(t);
            }
        };

        auto canBuild = [&](vector<string> words) -> int
        {
            vector<int> chars(26, 0);
            for (int i = 0; i < words.size(); i++)
            {
                for (int j = 0; j < words[i].length(); j++)
                {
                    chars[words[i][j] - 'a']++;
                }
            }

            int ret = 0;
            for (int i = 0; i < 26; i++)
            {
                if (chars[i] > freq[i])
                {
                    return -1;
                }
            }

            for (int i = 0; i < 26; i++)
            {
                ret += chars[i] * score[i];
            }
            return ret;
        };

        getCombinations();

        int mx = 0;
        for (auto k : posCombinations)
        {
            int ans = canBuild(k);
            if (ans != -1)
            {
                mx = max(mx, ans);
            }
        }
        return mx;
    }
};