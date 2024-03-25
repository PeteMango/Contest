#include <bits/stdc++.h>
using namespace std;

int A, B, C, D;

int main () {
  cin >> A >> B >> C >> D;
  cout << min(A, min(B, min(C, D))) << endl;
  cout << max(A, max(B, max(C, D))) << endl;
}