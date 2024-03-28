#include <iostream>
#include <vector>

using namespace std;

int main() {
  int N;
  vector<int> v;
  cin >> N;
  for (int i = 0, x; i < N; i++) {
    cin >> x;
    v.push_back(x);
  }
  int i = 0, ret = 0;
  while (i < N / 2) {
    if (v[i] == v[N / 2 + i]) {
      ret += 2;
    }
    i++;
  }
  printf("%d\n", ret);
}
