#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll N, K, A, B;
int main() {
  cin >> N >> K >> A >> B;
  if(N <= K) {
    cout << N * A << endl;
  }
  else {
    cout << K * A + (N - K) * B << endl;
  }
}