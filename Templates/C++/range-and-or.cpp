#include <iostream>
#include <vector>

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
