#include <bits/stdc++.h>
using namespace std;

int a, b, c, d;
int main() {
  cin >> a >> b >> c >> d;
  if(2*(a+b+c+1) + 2 - 2*b - 4*c == d) {
    cout << "C" << (a+b+c+1) << "H" << d << "\n";
  }
  else {
    cout << "invalid" << "\n";
  }
}