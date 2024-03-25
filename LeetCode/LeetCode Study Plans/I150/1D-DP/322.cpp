#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  int coinChange(vector<int> &coins, int amount) {
    if (amount == 0) {
      return 0;
    }

    vector<int> dp(amount + 1, 1e5 + 5);
    for (int i = 0; i < coins.size(); i++) {
      int t = coins[i];
      while (t <= amount) {
        dp[t] = min(dp[t], t / coins[i]);
        t += coins[i];
      }
    }

    for (int i = 0; i <= amount; i++) {
      for (int j = 0; j < coins.size(); j++) {
        if (i >= coins[j]) {
          dp[i] = min(dp[i], dp[i - coins[j]] + 1);
        }
      }
    }

    for (int i = 1; i <= amount; i++) {
      cout << dp[i] << " ";
    }
    cout << "\n";
    return dp[amount] == 100005 ? -1 : dp[amount];
  }
};

int main() {
  Solution s;
  // vector<int> coins = {1, 2, 5};
  // int amount = 11;

  vector<int> coins = {2};
  int amount = 3;

  cout << s.coinChange(coins, amount) << "\n";
}
