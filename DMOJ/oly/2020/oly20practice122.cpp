#include <bits/stdc++.h>
using namespace std;
const int MM = 1e5 + 5;
int N, a[MM];

bool sortable (int a[], int N) {
  int f=0, s=0, cnt=0;
  for(int i = 1; i < N; i++) {
    if(a[i] < a[i-1]) {
      cnt++;
      if(f == 0) {
        f = i;
      }
      else s = i;
    }
  }
  if(cnt > 2) return false;
  if(cnt == 0) return true;
  if(cnt == 2) swap(a[f-1], a[s]);
  else if(cnt == 1) swap(a[f-1], a[f]);
  for(int i = 1; i < N; i++) {
    if(a[i] < a[i-1]) {
      return false;
    }
  }
  return true;
}  

int main () {
  cin >> N;
  for(int i = 0; i < N; i++) {
    cin >> a[i];
  }
  if(sortable(a, N)) cout << "YES\n";
  else cout << "NO\n";
}