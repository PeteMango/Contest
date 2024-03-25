#include <bits/stdc++.h>
using namespace std;

#define LL long long

LL N;

LL odd_digits(LL n) { 
    if (n < 10) 
        return n; 
    else if (n / 10 < 10) 
        return 9; 
    else if (n / 100 < 10) 
        return 9 + n - 99; 
    else if (n / 1000 < 10) 
        return 909; 
    else if (n / 10000 < 10) 
        return 909 + n - 9999; 
    else if(n / 100000 < 10) {
      return 90909;
    }
    else if(n / 1000000 < 10) {
      return 90909 + n - 999999;
    }
    else if(n / 10000000 < 10) {
      return 9090909;
    }
    else if(n / 100000000 < 10) {
      return 9090909 + n - 99999999;
    }
    else if(n / 1000000000 < 10) {
      return 909090909;
    }
    else if(n / 10000000000 < 10) {
      return 909090909 + n - 9999999999;
    }
    else if(n / 100000000000 < 10) {
      return 90909090909;
    }
    else if(n / 1000000000000 < 10) {
      return 90909090909 + n - 999999999999;
    }
    else if(n / 10000000000000 < 10) {
      return 9090909090909;
    }
    else if(n / 100000000000000 < 10) {
      return 9090909090909 + n - 99999999999999;
    }
    else if(n / 1000000000000000 < 10) {
      return 909090909090909;
    }
    else if(n / 10000000000000000 < 10) {
      return 909090909090909 + n - 9999999999999999;
    }
    else if(n / 100000000000000000 < 10) {
      return 909090909090909;
    }
    else if(n / 1000000000000000000 < 10) {
      return 90909090909090909 + n - 999999999999999999;
    }
    else return 1;
}

int main () {
  cin >> N;
  cout << odd_digits(N) << "\n";
}