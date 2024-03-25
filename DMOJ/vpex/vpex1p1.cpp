#include <bits/stdc++.h>
using namespace std;

const int INF = 0x3f3f3f3f;
int A[5], B[5], SUMA, SUMB, MINA = INF, MINB = INF;

int main () {
  for(int i = 0; i < 5; i++) { scanf("%d", &A[i]); SUMA += A[i]; }
  for(int i = 0; i < 5; i++) { scanf("%d", &B[i]); SUMB += B[i]; }
  for(int i = 0; i < 5; i++) { 
    if(A[i] < MINA) MINA = A[i];
    if(B[i] < MINB) MINB = B[i];
  }
  printf("%d", max(SUMA - MINA, SUMB - MINB));
}