#include <bits/stdc++.h>
using namespace std;

int countTestedDevices(vector<int> &batteryPercentages)
{
    int numTested = 0, n = batteryPercentages.size();
    for (int i = 0; i < n; i++)
    {
        if (batteryPercentages[i] > 0)
        {
            numTested++;
            for (int j = i + 1; j < n; j++)
            {
                batteryPercentages[j]--;
            }
        }
    }
    return numTested;
}

int main()
{
    vector<int> v = {0, 1, 2};
    cout << countTestedDevices(v) << "\n";
}