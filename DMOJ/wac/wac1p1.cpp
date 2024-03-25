#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int T;
ll M, N;
int main() {
  cin >> T;
  for(int i = 0; i < T; i++) {
    cin >> M;
    N = sqrt(2 * M) + 1;
    if(N * (N - 1) / 2 >= M) {
      cout << N << endl;
    } 
    else cout << (int)(sqrt(2 * M) + 2) << endl;
  }
}