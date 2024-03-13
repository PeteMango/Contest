#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  int lengthOfLIS(vector<int> &nums) {
    int mx = 1;
    vector<int> dp(nums.size(), 1);
    for (int i = 0; i < nums.size(); i++) {
      for (int j = 0; j < i; j++) {
        if (nums[j] < nums[i]) {
          dp[i] = max(dp[i], dp[j] + 1);
        }
      }
    }
    cout << "dp is: \n";
    for (int i = 0; i < nums.size(); i++) {
      cout << dp[i] << " ";
    }
    cout << "\n";

    for (int i = 0; i < nums.size(); i++) {
      mx = max(mx, dp[i]);
    }
    return mx;
  }
};

int main() {
  Solution s;
  // vector<int> nums = {10, 9, 2, 5, 3, 7, 101, 18};

  // vector<int> nums = {0, 1, 0, 3, 2, 3};

  // vector<int> nums = {7, 7, 7, 7, 7, 7, 7};

  vector<int> nums = {1, 3, 6, 7, 9, 4, 10, 5, 6};

  cout << s.lengthOfLIS(nums) << "\n";
}
