#include <bits/stdc++.h>
using namespace std;

bool almostEqual(char a, char b)
{
    if (a == b || (int)(a)-1 == (int)(b) || (int)(b)-1 == (int)(a))
    {
        return true;
    }
    return false;
}

int removeAlmostEqualCharacters(string word)
{
    int n = word.length(), ans = 0, curLength = 1;
    for (int i = 1; i < n; i++)
    {
        if (almostEqual(word[i], word[i - 1]))
        {
            curLength++;
        }
        else
        {
            if (curLength > 1)
            {
                ans += curLength / 2;
            }
            curLength = 1;
        }
    }
    if (curLength > 1)
    {
        ans += curLength / 2;
    }
    return ans;
}

int main()
{
    string s = "zyxyxyz";
    cout << removeAlmostEqualCharacters(s) << "\n";
}