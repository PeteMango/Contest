#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> modifiedMatrix(vector<vector<int>> &matrix)
{
    vector<vector<int>> ans = matrix;
    for (int i = 0; i < matrix[0].size(); i++)
    {
        int mxElement = -1;
        for (int j = 0; j < matrix.size(); j++)
        {
            if (ans[j][i] > mxElement)
            {
                mxElement = ans[j][i];
            }
        }

        for (int j = 0; j < matrix.size(); j++)
        {
            if (ans[j][i] == -1)
            {
                ans[j][i] = mxElement;
            }
        }
    }
    return ans;
}

int main()
{
    vector<vector<int>> m = {
        {1, 2, -1},
        {4, -1, 6},
        {7, 8, 9},
    };

    vector<vector<int>> m2 = {
        {3, -1},
        {5, 2},
    };

    vector<vector<int>> ans = modifiedMatrix(m2);
    for (int i = 0; i < ans.size(); i++)
    {
        for (int j = 0; j < ans[0].size(); j++)
        {
            cout << ans[i][j] << " ";
        }
        cout << "\n";
    }
}