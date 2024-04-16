#include <functional>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  long long findKthSmallest(vector<int> &coins, int k) {
    sort(coins.begin(), coins.end());

    auto countOnes = [&](int mask) -> int {
      int cnt = 0;
      while (mask > 0) {
        cnt++;
        mask = mask & (mask - 1);
      }
      return cnt;
    };

    auto numCanMake = [&](long long val) -> long long {
      long long ans = 0;
      int bitmask = (1 << coins.size()) - 1;

      /*
        check for all permutations with bitmask
      */
      for (int i = 1; i <= bitmask; i++) {
        long long lcmOfSetBits = 1;
        for (int j = 0; j < coins.size(); j++) {
          if (i & (1 << j)) {
            /*
              only get the lcm if the jth bit is set in the current mask
              check with i & (1 << j)
            */
            lcmOfSetBits = lcm(coins[j], lcmOfSetBits);
          }
        }

        /*
            if odd it adds to ans, else it subtracts from ans
            [3, 6, 9] = [3] + [6] + [9] - [3, 6] - [3, 9] - [6, 9] + [3, 6, 9]
        */

        if (countOnes(i) % 2 == 1) {
          ans += val / lcmOfSetBits;
        } else {
          ans -= val / lcmOfSetBits;
        }
      }
      return ans;
    };

    long long l = 0, r = 2e13 + 5, ans = 0;
    while (l <= r) {
      long long mid = (l + r) / 2;
      long long canMake = numCanMake(mid);
      if (canMake >= k) {
        ans = mid;
        r = mid - 1;
      } else if (canMake < k) {
        l = mid + 1;
      }
    }
    return ans;
  }
};

int main() {
  Solution s;

  vector<int> tc1 = {3, 6, 9};
  int k1 = 3;

  vector<int> tc2 = {5, 2};
  int k2 = 7;

  vector<int> tc3 = {6, 1, 2, 4};
  int k3 = 4;

  cout << s.findKthSmallest(tc1, k1) << "\n";
  cout << s.findKthSmallest(tc2, k2) << "\n";
  cout << s.findKthSmallest(tc3, k3) << "\n";

  return 0;
}
