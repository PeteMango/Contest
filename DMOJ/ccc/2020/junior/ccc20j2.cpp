#include <bits/stdc++.h>
using namespace std;
int P, N, R, I, T, C;

int main () {
  scanf("%d%d%d", &P, &N, &R);
  I = N; T = N;
  while(T <= P) {
    I *= R;
    T += I;
    C++;
    // cout << I << " " << T << " " << C << endl;
  }
  printf("%d", C);
}