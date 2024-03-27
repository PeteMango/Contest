#include <iostream>

using namespace std;

int main() {
  int D;
  cin >> D;
  while (true) {
    int x;
    cin >> x;
    if (x >= D) {
      break;
    } else {
      D += x;
    }
  }

  printf("%d\n", D);
}
