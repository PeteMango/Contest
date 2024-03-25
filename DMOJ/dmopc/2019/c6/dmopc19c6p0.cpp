#include <bits/stdc++.h>
using namespace std;
int a, b, c;
int main () {
  scanf("%d%d%d",&a, &b, &c);
  if(a + b <= c || a + c <= b || b + c <= a) {
    printf("%s", "no");
  }
  else {
    printf("%s", "yes");
  }
}