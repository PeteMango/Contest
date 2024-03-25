#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e6+5, NINF = INT_MIN;
int N, Q, JAMES[MAXN], EDWARD[MAXN], ARR[MAXN];
int main () {
  cin.tie(0);
  cin.sync_with_stdio(0);
  cin >> N >> Q;
  for(int i = 1; i <= N; i++) {
    cin >> ARR[i];
  }
  int mx = INT_MIN;
  for(int i = 1; i <= N; i++) {
    if(ARR[i] > mx){
      JAMES[i] = i;
    } 
    else JAMES[i] = JAMES[i - 1];
    mx=max(mx, ARR[i]);
  }
  mx = ARR[N]; EDWARD[N] = N;
  for(int i = N-1; i>0; i--) {
    if(ARR[i] > mx) {
      EDWARD[i] = i;
    }
    else EDWARD[i] = EDWARD[i + 1];
    mx=max(mx, ARR[i]);
  }
  // for(int i = 1; i <= N; i++) {
  //   cout << JAMES[i] << " " << EDWARD[i] << endl;
  // }
  for(int i = 1, C; i <= Q; i++) {
    cin >> C;
    cout << JAMES[C-1] << " " << EDWARD[C + 1] << "\n";
  }
}
