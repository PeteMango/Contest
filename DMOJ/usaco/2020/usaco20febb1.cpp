#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
LL N;

int main() {
  cin >> N;
  vector<LL> X(N, 0), Y(N, 0);
  for(LL i = 0; i < N; i++) {
    cin >> X[i] >> Y[i];
  }
  LL best = -1;
  for(LL i = 0; i < N; i++) {
    for(LL j = 0; j < N; j++) {
      for(LL k = 0; k < N; k++) {
        if(Y[i] == Y[j] && X[i] == X[k]) {
          LL area = (X[j] - X[i]) * (Y[k] - Y[i]);
          if(area < 0) { area *= -1; }
          if(area > best) {
            best = area;
          }
        }
      }
    }
  }
  cout << best << endl;
}