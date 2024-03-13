#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  int climbStairs(int n) {
    if (n <= 2) {
      return n;
    }
    vector<int> dp(n + 1, 0);

    function<int()> steps = [&]() -> int {
      dp[1] = 1;
      dp[2] = 2;
      for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 2] + dp[i - 1];
      }
      return dp[n];
    };

    /*
    3:
    1 2
    2 1
    1 1 1

    4:
    1 1 1 1
    2 2
    1 1 2
    2 1 1
    1 2 1
    */

    return steps();
  }
};

int main() {
  Solution s;
  int n = 5;

  cout << s.climbStairs(n) << endl;
}
