#include <bits/stdc++.h>
using namespace std;
#define LL long long
LL E, V, O, L;
string s;

int main() {
  cin >> s;
  for(int i = (int)s.size() - 1; i >= 0; i--) {
    if(s[i]=='e') E++;
    else if(s[i]=='v') V += E;
    else if(s[i]=='o') O += V;
    else if(s[i]=='l') L += O;
  }
  cout << L << "\n";
}