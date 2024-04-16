#include <functional>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  int maximumPrimeDifference(vector<int> &nums) {
    auto isPrime = [&](int num) -> bool {
      if (num == 1) {
        return false;
      }
      for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) {
          return false;
        }
      }
      return true;
    };

    vector<int> index;
    for (int i = 0; i < nums.size(); i++) {
      if (isPrime(nums[i])) {
        index.push_back(i);
      }
    }

    if (index.size() == 1) {
      return 0;
    }
    return index[index.size() - 1] - index[0];
  }
};

int main() {
  Solution s;

  vector<int> tc1 = {4, 2, 9, 5, 3};
  vector<int> tc2 = {4, 8, 2, 8};
  vector<int> tc3 = {1, 7};

  cout << s.maximumPrimeDifference(tc1) << "\n";
  cout << s.maximumPrimeDifference(tc2) << "\n";
  cout << s.maximumPrimeDifference(tc3) << "\n";

  return 0;
}
