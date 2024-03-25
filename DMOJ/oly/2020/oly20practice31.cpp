#include <bits/stdc++.h>
using namespace std;
#define pb push_back
int N, M, R;
struct Job {
  int x, y, p;
};

const int MM = 1000005;
Job arr[MM];

bool jobComparator (Job a, Job b) {
  return (a.y < b.y);
}

int nonConflict (int idx) {
  for(int j = idx-1; j >= 0; j--) {
    if(arr[j].y <= arr[idx].x) {
      return j;
    }
  }
  return -1;
}

int maxProfit (int size) {
  sort(arr, arr+size, jobComparator);
  int *table = new int[N];
  table[0] = arr[0].p;
  for(int i = 1; i < N; i++) {
    int includeProfit = arr[i].p, L = nonConflict(i);
    if(L != -1) {
      includeProfit += table[L];
    }
    table[i] = max(includeProfit, table[i - 1]);
  }
  return table[N - 1];
}

int main () {
  scanf("%d%d%d", &N, &M, &R);
  for(int i = 0, x, y, p; i < M; i++){
    scanf("%d%d%d", &x, &y, &p);
    arr[i].x = x; arr[i].y = y+R; arr[i].p = p;
  } 
  printf("%d\n", maxProfit(N));
}
