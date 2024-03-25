#include <bits/stdc++.h>
using namespace std;

#define LD long double
#define LL long long

const LL MOD = 1e9 + 7;
int T;
LD a, b, c;
LL N;

LL power (LL base, LL exp) {
  LL t = 1L;
  while(exp > 0) {
    if(exp % 2 != 0) {
      t = (t * base) % MOD;
    }
    base = (base * base) % MOD;
    exp /= 2;
  }
  return t % MOD;
}

int main() {
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cin >> a >> b >> c >> N;
    if(b/a == c/b) {
      LL multiplyer = (LL) b/a;
      cout << (LL) (c * power(multiplyer, N-3)) % MOD << "\n";
    }
    else if(b-a == c-b) {
      LL difference = (LL) b-a;
      cout << (LL) (c + (difference * (N-3))) % MOD << "\n";
    }
  }
}