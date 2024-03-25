#include <bits/stdc++.h>
using namespace std;
int N;

int sumFact (int x) {
  int ret=0;
  for(int i = 1; i < x; i++) {
    if(x % i == 0) {
      ret += i;
    }
  }
  return ret;
}

bool isPerfect (int x) {
  if(sumFact(x) == x) {
    return true;
  }
  return false;
}

bool isDeficient (int x) {
  if(sumFact(x) < x) {
    return true;
  }
  return false;
}

int main() {
  cin >> N;
  for(int i = 1, M; i <= N; i++) {
    cin >> M;
    if(isPerfect(M)) {
      cout << M << " is a perfect number.\n";
    }
    else if(isDeficient(M)) {
      cout << M << " is a deficient number.\n";
    }
    else cout << M << " is an abundant number.\n";
  }
}