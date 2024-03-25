#include <bits/stdc++.h>
using namespace std;

int N; 
string s;

int main () {
  cin >> N >> s;
  for(int i = 1; i <= N; i++) {
    bool flg = false;
    for(int j = 0; j + i <= N; j++) {
      for(int k = 0; k < j; k++) {
        if(s.substr(j, i) == s.substr(k, i)){
          flg = true;
        }
      }
    }
    if(flg == false) {
      cout << i << endl;
      break;
    }
  }
}