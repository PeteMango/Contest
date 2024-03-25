#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e5;
typedef long long ll;
ll SUM = 0, CNT = 0;
int N, B;
struct node {ll p, s, t, h;} arr[MAXN];

bool sortBySum(node a, node b) { 
    return (a.t > b.t); 
} 

int main() {
  cin >> N >> B;
  for(int i = 0; i < N; i++){
    cin >> arr[i].p >> arr[i].s;
    arr[i].t = arr[i].p + arr[i].s;
    arr[i].h = arr[i].p/2 + arr[i].s;
  }
  sort(arr, arr+sizeof(arr)/sizeof(arr[0]), sortBySum);
  // for(int i = 0; i < N; i++) {
  //   cout << arr[i].t << endl;
  // }
  for(int i = N - 1; i >= 0; i--){
    if(SUM + arr[i].t <= B) {
      SUM += arr[i].t;
      CNT++;
    }
    else {
      if(SUM + arr[i].h <= B){
        SUM += arr[i].h;
        CNT++;
      }
    }
  }
  cout << CNT << endl;
}
