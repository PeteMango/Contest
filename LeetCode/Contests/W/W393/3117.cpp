#include <functional>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <vector>
using namespace std;

class RangeAndOrQueries {
public:
  RangeAndOrQueries(const std::vector<int> &arr) {
    MAX = 100000;
    bitscount = 32;
    prefix_count.resize(bitscount, std::vector<int>(MAX, 0));
    find_prefix_count(arr);
  }

  void find_prefix_count(const std::vector<int> &arr) {
    int n = arr.size();
    for (int i = 0; i < bitscount; ++i) {
      prefix_count[i][0] = ((arr[0] >> i) & 1);
      for (int j = 1; j < n; ++j) {
        prefix_count[i][j] = ((arr[j] >> i) & 1) + prefix_count[i][j - 1];
      }
    }
  }

  int range_and(int l, int r) {
    int ans = (1 << 31) - 1; // Initialize answer with all bits set to 1
    for (int i = 0; i < bitscount; ++i) {
      int x = 0;
      if (l == 0) {
        x = prefix_count[i][r];
      } else {
        x = prefix_count[i][r] - prefix_count[i][l - 1];
      }
      if (x != r - l + 1) {
        ans &= ~(1 << i);
      }
    }
    return ans;
  }

  std::vector<int>
  multiple_range_and_queries(const std::vector<std::vector<int>> &queries) {
    std::vector<int> results;
    for (const auto &query : queries) {
      results.push_back(range_and(query[0], query[1]));
    }
    return results;
  }

private:
  int MAX;
  int bitscount;
  std::vector<std::vector<int>> prefix_count;
};

class Solution {
public:
  int minimumValueSum(vector<int> &nums, vector<int> &andValues) {
    RangeAndOrQueries rq(nums);
    int n = nums.size(), m = andValues.size();
    if (m == 1) {
      return rq.range_and(0, n - 1) == andValues[0] ? nums[n - 1] : -1;
    }
    int dp[n + 1][m + 1];
    memset(dp, 0, (n + 1) * (m + 1) * sizeof(int));
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        int x = n + 1, y = -1;
        for (int k = 0; k <= i; k++) {
          if (rq.range_and(k, i) == andValues[j]) {
            x = min(x, k);
            y = max(y, k);
          }
        }
        for (int z = x; z <= y; z++) {
          dp[i][j] = min(dp[i][j], dp[i - z][j - 1] + nums[i - 1]);
        }
      }
    }
  }
};

int main() {
  Solution s;
  return 0;
  // i gave up
}
