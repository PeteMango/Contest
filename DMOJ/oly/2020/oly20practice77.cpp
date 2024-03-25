#include <bits/stdc++.h>
using namespace std;
const int MM = 3e5 + 5, INF = 0x3f3f3f3f;
int N, mn = INF, L[MM], R[MM];
string Line;

/*
L = 0
R = 1
*/
int main() {
  cin >> N >> Line;
  for(int i = 0; i < MM; i++) {
    L[i] = 0;
    R[i] = 0;
  }
  if(Line[0] == 'L') {
    L[0] = 1;
  }
  else {
    R[0] = 1;
  }
  for(int i = 1; i <= N; i++) {
    if(Line[i] == 'L') {
      L[i] = L[i-1] + 1;
      R[i] = R[i-1];
    } 
    else {
      R[i] = R[i-1] + 1;
      L[i] = L[i-1];
    }
  }
  // for(int i = 0; i < N; i++) {
  //   cout << L[i] << " " << R[i] << "\n";
  // }
  for(int i = 0; i < N; i++) {
    mn = min(mn, (L[i-1])+(R[N-1]-R[i]));
  }
  cout << mn << "\n";
}