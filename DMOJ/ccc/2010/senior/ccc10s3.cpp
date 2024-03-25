#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int LENGTH = 1000000, N, M, arr[1000005];

int compute (int j, int mid) {
    int curr = j, hydrants = 1;
    for (int i = j; i < N + j; i++)
      if (arr[i] - arr[curr] > 2 * mid) {
        curr = i;
        hydrants++;
      }
    return hydrants;
  }

int possible (int mid) {
    int hydrants = 1000005;
    for (int i = 0; i < fmin(N, 10); i++){
      hydrants = min(hydrants, compute(i, mid));
    }
    return hydrants;
}


int main() {
  scanf("%d", &N);
  for(int i = 0; i < N; i++){
    scanf("%d", &arr[i]);
  }
  sort(arr, arr+N);
  for(int i = 0; i < N; i++){
    arr[i + N] = arr[i] + LENGTH;
  }
  scanf("%d", &M);
  int l = 0, r = LENGTH;
  while(l <= r){
    int mid = (l + r) / 2;
    if(M >= possible(mid)){
      r = mid-1;
    }
    else l = mid + 1;
  }
  printf("%d\n", l);
}