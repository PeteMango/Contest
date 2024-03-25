#include <bits/stdc++.h>
using namespace std;
int S, M, L;

int main () {
  scanf("%d%d%d", &S, &M, &L);
  if(S + 2 * M + 3 * L >= 10) {
    printf("%s", "happy");
  }
  else {
    printf("%s", "sad");
  }
}