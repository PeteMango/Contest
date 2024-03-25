#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
#define str string
str a, b;
LL sum=0;

int main() {
  cin >> a >> b;
  for(int i = 0; i < a.length(); i++) {
    for(int j = 0; j < b.length(); j++) {
      sum += (a[i]-'0') * (b[j]-'0');
    }
  }
  cout << sum << "\n";
}