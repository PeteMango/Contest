#include <bits/stdc++.h>
using namespace std;
string s;
int indexA = -1, indexZ = -1;

int main() {
  cin >> s;
  for(int i = 0; i < s.length(); i++) {
    if(s[i] == 'A') {indexA = i; break;}
  }
  for(int i = s.length() - 1; i >= 0; i--) {
    if(s[i] == 'Z') {indexZ = i; break;}
  }
  cout << (indexZ-indexA+1) << endl;
} 