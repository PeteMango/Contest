#include <bits/stdc++.h>
using namespace std;
const int MM = 50005;
#define pb push_back
#define f first
#define s second
int T, N, curPos=0, cnT=0;
vector< pair <int,int> > v;

int main() {
  scanf("%d%d", &T, &N);
  for(int i = 1, D; i <= N; i++) {
    scanf("%d", &D);
    v.pb(make_pair(abs(D), D));
  }
  sort(v.begin(), v.end());
  // for(int i = 0; i < v.size(); i++) {
  //   printf("%d %d\n", v[i].f, v[i].s);
  // }
  // for(int i = 0; i < v.size(); i++) {
  //   printf("%d", v[i].f);
  // }
  for(int i = 0; i < v.size(); i++) {
    if(T - (abs(v[i].s - curPos)) >= 0) {
      T -= abs(v[i].s - curPos);
      curPos = v[i].s;
      cnT++;
    }
    else {
      break;
    }
  }
  printf("%d", cnT);
}