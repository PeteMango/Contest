#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int N, L;
string s[1005];
int main() {
  cin >> N >> L;
  for(int i = 0; i < N; i++){
    cin >> s[i];
  }
  sort(s, s+sizeof(s)/sizeof(s[0]));
  string ans = "";
  for(int i = 1004; i >= (1004-N); i--){
    ans += s[i];
  }
  cout << ans << endl;
}