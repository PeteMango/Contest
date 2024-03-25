#include <bits/stdc++.h>
using namespace std;
const int T = 10, MM = 1005;
int N;

int main() {
  for(int x = 1; x <= T; x++) {
    cin >> N; vector<int> v(N);
    for(int i = 0; i < N; i++) {
      cin >> v[i];
    }
    int t = N, suM=0;
    for(int i = N-1; i >= 0; i--) {
      if(v[i] == t) {
        t--;
      }
    }
    for(int i = t; i > 0; i--) {
      int idx = find(v.begin(), v.end(), i) - v.begin();
      v.erase(v.begin()+idx);
      v.insert(v.begin(), i);
      suM += idx;
    }
    cout << suM << "\n";
  }
}