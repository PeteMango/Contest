#include <bits/stdc++.h>
using namespace std;
int N;
double x, sum;

int main () {
  cin >> N;
  for(int i = 1; i <= N; i++) {
    cin >> x;
    sum += x;
  }
  printf("%.1f\n", sum/(double)N);
}