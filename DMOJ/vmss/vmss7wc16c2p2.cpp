#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e5 + 5;
string s;
int Q, psa[MAXN];

int main () {
  cin >> s >> Q;
  if(s[0] == 'G') psa[0] = 1;
  for(int i = 1; i < s.length(); i++){
    psa[i] += psa[i - 1];
    if(s[i] == 'G') psa[i]++;
  }
  for(int i = 0, L, R; i < Q; i++){
    scanf("%d %d", &L, &R);
    cout << psa[R] - psa[L - 1] << endl;
  }
}