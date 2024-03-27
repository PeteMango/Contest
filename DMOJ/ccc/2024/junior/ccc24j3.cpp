#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {
  int N;
  cin >> N;
  unordered_map<int, int> mp;
  for (int i = 0, x; i < N; i++) {
    cin >> x;
    if (mp.find(x) != mp.end()) {
      mp[x] += 1;
    } else {
      mp[x] = 1;
    }
  }

  vector<int> v;
  for (auto p : mp) {
    v.push_back(p.first);
  }

  sort(v.begin(), v.end());

  printf("%d %d\n", v[v.size() - 3], mp[v[v.size() - 3]]);
}
