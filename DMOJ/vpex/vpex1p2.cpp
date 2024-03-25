#include <bits/stdc++.h>
using namespace std;

const int MAXN = 15;
int N, A[MAXN], SUM, CNT;

int main () {
  scanf("%d", &N);
  for(int i = 0; i < N; i++) { scanf("%d", &A[i]); SUM += A[i]; }
  SUM /= N;
  for(int i = 0; i < N; i++) { 
    if(A[i] != SUM) CNT++;
  }
  printf("%d", CNT);
}