#include <bits/stdc++.h>
using namespace std;
int N, v;

bool isPrime (int x) {
  for(int i = 2; i <= sqrt(x); i++) {
    if(x % i == 0) {
      return false;
    }
  }
  return true;
}

int main () {
  scanf("%d", &N);
  for(int i = 1; i <= N; i++) {
    scanf("%d", &v);
    for(int j = 1; j <= v; j++) {
      if(isPrime(v+j) && isPrime(v-j)) {
        cout << (v+j) << " " << (v-j) << "\n";
        break;
      }
    }
  }
}