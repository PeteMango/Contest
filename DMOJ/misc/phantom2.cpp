#include <bits/stdc++.h>
using namespace std;

int N;
bool sieve[1000002];
int main() {
  memset(sieve, true, sizeof(sieve));
  sieve[1] = false;
  for (int p = 2; p * p < 1000002; p++) { 
        if (sieve[p] == true) { 
            for (int i = p + p; i < 1000002; i += p) {
                sieve[i] = false; 
            }
        } 
    } 
  scanf("%d", &N);
  for(int i = 0, a, b; i < N; i++){
    int cnt = 0;
      scanf("%d %d", &a, &b);
      if(a > b){
        int t = a;
        a = b;
        b = t;
      }
      for(int j = a; j < b; j++){
        if(sieve[j] == true) cnt++;
      }
      printf("%d\n", cnt);
  }
}