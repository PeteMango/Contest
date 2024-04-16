#include <functional>
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
  void test() {
    /*
    Returns the number of set bits in a number

    Args:
      binary (int): the number to calculate bits for

    Returns:
        set-bits (int): number of set bits
    */
    auto countSetBits = [&](int binary) -> int {
      int cnt = 0;
      while (binary > 0) {
        cnt++;
        binary = binary & (binary - 1);
      }
      return cnt;
    };

    cout << countSetBits(7) << "\n";
  }
};

int main() {
  Solution s;
  s.test();
}
