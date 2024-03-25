#include <bits/stdc++.h>
using namespace std;

#define LL long long

LL x, y, A, B;

LL countDivisible (LL x, LL y, LL M) {
  if(x % M == 0) return (y/M) - (x/M) + 1;
  else return (y/M) - (x/M);
}

LL GCD (LL a,  LL b) {
  if(b == 0) return a;
  return GCD(b, a%b);
}

LL LCM (LL a, LL b) {
  return (a/GCD(a, b) * b);
}

int main () {
  cin >> x >> y >> A >> B;
  cout << countDivisible(x, y, A) + countDivisible(x, y, B) - countDivisible(x, y, LCM(A, B)) << "\n";
}