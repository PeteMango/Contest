#include <bits/stdc++.h>
using namespace std;

int areaOfMaxDiagonal(vector<vector<int>> &dimensions)
{
    if (dimensions.size() == 0)
    {
        return 0;
    }
    int mxArea = 0;
    double mxDiagonal = -1;
    for (auto v : dimensions)
    {
        int l = v[0], h = v[1];
        if (sqrt(l * l + h * h) == mxDiagonal)
        {
            if (l * h > mxArea)
            {
                mxArea = l * h;
            }
        }

        if (sqrt(l * l + h * h) > mxDiagonal)
        {
            mxArea = l * h;
            mxDiagonal = sqrt(l * l + h * h);
        }
    }
    return mxArea;
}

int main()
{
    vector<vector<int>> v = {{6, 5}, {8, 6}, {2, 10}, {8, 1}, {9, 2}, {3, 5}, {3, 5}};
    cout << areaOfMaxDiagonal(v) << "\n";
}