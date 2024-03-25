#include <bits/stdc++.h>
using namespace std;

/* 
https://en.wikipedia.org/wiki/Bayes%27_theorem
Bayes' Theorem --> P(A, B) - What is the Probablitiy of A if B is true
Final Answer = Average of All dP elements of ( sum (dP[i] / N) )

Case 1: b[i] == b[i] --> dP[i] = 1; Josh will have 100% chance to get his burger
Case 2: b[j] == b[i] && j > i --> dP[i] = dP[j] jth person ordered the same burger as the ith person
Case 3: dP[i] = (1 + dP[i+1] + dP[i+2] + dP[N])/(N - i + 1);

Sample Case: 
7 
1 2 3 1 1 2 3

b[] = {1, 2, 3, 1, 1, 2, 3}
dP[] = {1, 1/2, 0, 1, 1, 0.5, 0}
Ans = 4/7
*/

const int MM =  1000005;
int N, Lst[MM], b[MM];
double dP[MM], suM;

int main () {
  scanf("%d", &N);
  for(int i = 1; i <= N; i++) {
    scanf("%d", &b[i]);
    Lst[b[i]] = i;
  }
  dP[N] = (b[N] == b[1]? 1.0:0.0);
  suM += dP[N];
  for(int i = N-1; i >= 1; i--) {
    if(b[i] == b[1]) {
      dP[i] = 1.0;
    }
    else if(Lst[b[i]] != i) {
       dP[i] = dP[Lst[b[i]]];
    }
    else if(Lst[b[i]] == i) {
      dP[i] = (1+suM)/(N-i+1);
    }
    suM += dP[i];
  }
  printf("%.9f\n", suM/N);
}