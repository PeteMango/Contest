#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  int rob(vector<int> &nums) {
    if (nums.size() == 1) {
      return nums[0];
    } else if (nums.size() == 2) {
      return max(nums[0], nums[1]);
    }

    vector<int> dp(nums.size() + 1, 0);
    dp[0] = 0;
    dp[1] = nums[0];

    auto max_value = [&]() -> int {
      for (int i = 1; i < nums.size(); i++) {
        dp[i + 1] = max(dp[i - 1] + nums[i], dp[i]);
      }
      return dp[nums.size()];
    };
    return max_value();
  }
};

int main() {
  Solution s;
  vector<int> nums1 = {1, 2, 3, 1};
  vector<int> nums2 = {2, 7, 9, 3, 1};
  vector<int> nums3 = {2, 1, 1, 2};

  cout << s.rob(nums3) << "\n";
}
