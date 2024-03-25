#include <bits/stdc++.h>
using namespace std;
#define str string
#define pb push_back
const int MM = 1e5 + 5;

vector<pair<int, str>> v;
int N, medIdx, mark;
string s;

int main () {
  cin >> N;
  for(int i = 1; i <= N; i++) {
    cin >> s >> mark;
    v.pb({mark, s});
  }
  sort(v.begin(), v.end());
  if(N % 2 == 0) medIdx = N/2-1;
  else medIdx = N/2;
  cout << v[medIdx].second << "\n";
}