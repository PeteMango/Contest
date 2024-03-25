#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int a, b, c, d;
int main() {
  scanf("%d %d %d %d", &a, &b, &c, &d);
  if(a == b && b == c && c == d) cout << "Fish At Constant Depth" << endl;
  else if(a > b && b > c && c > d) cout << "Fish Diving" << endl;
  else if(a < b && b < c && c < d) cout << "Fish Rising" << endl;
  else cout << "No Fish" << endl;
}