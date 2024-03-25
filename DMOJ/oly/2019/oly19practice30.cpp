#include <bits/stdc++.h>
using namespace std;
#define str string
const int MM = 105;
int N, M;
str s, G[MM][MM];

int main () {
  cin >> N >> M;
  for(int i = 0; i < N; i++) {
    cin >> s;
    for(int j = 0; j < M; j++) {
      G[i][j] = s[j];
    }
  }
  for(int i = 0; i <= M+1; i++) cout << "#";
  cout << "\n";
  for(int i = 0; i < N; i++) {
    cout << "#";
    for(int j = 0; j < M; j++) {
      cout << G[i][j];
    }
    cout << "#\n";
  }
  for(int i = 0; i <= M+1; i++) cout << "#";
  cout << "\n";
}