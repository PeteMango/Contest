/* Mon, April 29, 2024 */

class Solution {
public:
string binary(unsigned x)
{
    string s;
    do
    {
        s.push_back('0' + (x & 1));
    } while (x >>= 1);
    reverse(s.begin(), s.end());
    return s;
}

int minOperations(vector<int> &nums, int k)
{
    int XOR = nums[0];
    for (int i = 1; i < nums.size(); i++)
    {
        XOR ^= nums[i];
    }

    // cout << "XOR IS: " << XOR << "\n";

    string b = binary(XOR), r = binary(k);

    // cout << "B & R IS: " << b << " " << r << "\n";

    int d = 0;

    if (b.size() == r.size())
    {
    }
    else if (b.size() < r.size())
    {
        int pad = r.size() - b.size();
        string t = "";
        for (int i = 0; i < pad; i++)
        {
            t += "0";
        }
        b = t + b;
    }
    else if (r.size() < b.size())
    {
        int pad = b.size() - r.size();
        string t = "";
        for (int i = 0; i < pad; i++)
        {
            t += "0";
        }
        r = t + r;
    }

    // cout << b << " " << r << "\n";

    for (int i = 0; i < r.size(); i++)
    {
        d += (b[i] == r[i]) ? 0 : 1;
    }
    return d;
}

};