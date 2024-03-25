#include <bits/stdc++.h>
using namespace std;
int N;
vector<int> v, d;

void clear () {
  v.clear();
  d.clear();
}

int main() {
  while(true) {
    cin >> N;
    if(N == 0) break;
    for(int i = 1, x; i <= N; i++) {
      cin >> x;
      v.push_back(x);
    }
    if(N == 1) {
      cout << "0\n";
      continue;
    }
    for(int i = 0; i < N-1; i++) {
      d.push_back(v[i+1] - v[i]);
    }
    for(int i = 0; i < N-1; i++) {
      bool f = true;
      for(int j = i+1, k = 0; j < N-1; j++, k++) {
        if(k > i) k = 0;
        if(d[j] != d[k]) {
          f = false;
          break;
        }
      }
      if(f) {
        cout << i+1 << "\n";
        break;
      }
    }
    clear();
  }
}
