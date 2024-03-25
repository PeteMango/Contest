#include <iostream>
#include <bits/stdc++.h>
using namespace std;

struct node{int x, y, idx;}
arr[50005];

int N, M;

bool compare(node a, node b){
  return (a.x < b.x);
}
int main(){
  scanf("%d %d", &N, &M);
  for(int i = 0; i < N; i++){
    scanf("%d %d", &arr[i].x, &arr[i].y);
    arr[i].idx = i;
  }
  sort(arr, arr+sizeof(arr)/sizeof(arr[0]), compare);
  // for(int i = 50004; i >= (50004 - M); i--){
  //   cout << arr[i].x << " " << arr[i].y << " " << arr[i].idx << endl;
  // }
  int max = -1, idx = 0;
  for(int i = 50004; i > (50004 - M); i--){
    if(arr[i].y > max){
      max = arr[i].y;
      idx = arr[i].idx;
    }
  }
  cout << (idx+1) << endl;
}