#include <bits/stdc++.h>
using namespace std;
const int INF = INT_MAX;
#define f first
#define s second
#define pb push_back
int A, B;

int findPowerOfK (int N, int K) { 
  int cnT = 0, R = K;
  while(R <= N) {
    cnT += (N/R);
    R *= K;
  }
  return cnT;
}

vector<pair<int, int> > primeFactor (int N) {
  vector<pair<int, int> > ret;
  for(int i = 2; N != 1; i++) {
    if(N % i == 0) {
      int cnT=0;
      while(N % i == 0) {
        N /= i;
        cnT++;
      }
      ret.pb(make_pair(i, cnT));
    }
  }
  return ret;
}

int powerOfN (int N, int K) {
  vector<pair<int, int> > primeFactors; 
  int anS = INF;
  primeFactors = primeFactor(K);
  for(int i = 0; i < primeFactors.size(); i++) {
    anS = min(anS, findPowerOfK(N, primeFactors[i].f)/primeFactors[i].s);
  }
  return anS;
}

int main () {
  scanf("%d%d", &A, &B);
  printf("%d\n", powerOfN(B, A));
}