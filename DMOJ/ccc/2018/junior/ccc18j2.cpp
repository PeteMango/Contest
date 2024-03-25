#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int N, cnt = 0;
string a, b;
int main() {
  cin >> N >> a >> b;
  for(int i = 0; i < N; i++){
    if(a[i] == b[i] && a[i] == 'C' && b[i] == 'C'){
      cnt++;
    }
  }
  cout << cnt << endl;
}