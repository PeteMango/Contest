#include <bits/stdc++.h>
using namespace std;

int minimumOperationsToMakeEqual(int x, int y)
{
    queue<pair<int, int>> q;
    unordered_set<int> vis;

    q.push({x, 0});

    while (!q.empty())
    {
        int curNum = q.front().first, numOp = q.front().second;
        q.pop();

        if (curNum == y)
        {
            return numOp;
        }

        if (vis.find(curNum) != vis.end())
        {
            continue;
        }
        vis.emplace(curNum);

        if (curNum - 1 >= 0)
        {
            q.push({curNum - 1, numOp + 1});
        }

        q.push({curNum + 1, numOp + 1});

        if (curNum % 5 == 0)
        {
            q.push({curNum / 5, numOp + 1});
        }

        if (curNum % 11 == 0)
        {
            q.push({curNum / 11, numOp + 1});
        }
    }
    return -1;
}
int main()
{
    int x = 26, y = 1;
    cout << minimumOperationsToMakeEqual(x, y) << "\n";
}
