#include <bits/stdc++.h>
using namespace std;

int main(){
  vector<int> arr(10000005);
  for (int x = 2; x < 10000005; x++){
        if (!arr[x]){
            arr[x]++;
            for (int y = x + x; y < 10000005; y += x){
               arr[y]++;
          } 
     }
}
int N;
scanf("%d", &N);
for (int x = 1, a, b, k; x <= N; x++){
       scanf("%i%i%i", &a, &b,&k);
       int cnt = 0;
       for (int y = a; y <= b; y++){
         cnt += (arr[y] == k);
      }
      printf("Case #%i: %i\n", x, cnt);
  }
  return 0;
}