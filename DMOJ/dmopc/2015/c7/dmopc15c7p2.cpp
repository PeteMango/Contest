#include <bits/stdc++.h>
using namespace std;

int cnt=0;
string s;

int main () {
  getline(cin, s);
  for(int i = 0; i < s.length(); i++) {
    if(s[i] == ' ') {
      cnt++;
    }
  }
  cout << cnt+1 << "\n";
}