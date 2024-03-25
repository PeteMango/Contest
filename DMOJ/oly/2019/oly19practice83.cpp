#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll A, B, X, CNT = 0, F, L;
int main () {
  cin >> A >> B >> X;
  if(A % X == 0) {
    F = A;
  }
  else {
    for(ll i = A; i <= A + X; i++) {
      if(i % X == 0) {
        F = i;
        break;
      }
    }
  }
  if(B % X == 0) {
    L = B;
  }
  else {
    for(ll i = B; i >= B - X; i--) {
      if(i % X == 0) {
        L = i;
        break;
      }
    }
  }
  cout << (L - F)/X + 1 << endl;
}