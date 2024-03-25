#include <bits/stdc++.h>
using namespace std;
const int MM = 1e5 + 5;
int Q, a, b, sum[MM];
bool prime[MM]; 

void sieve () { 
    memset(prime, true, sizeof(prime)); 
    for (int i = 2; i*i < MM; i++)  { 
      if (prime[i] == true) { 
        for (int j = i * 2; j < MM; j += i) 
          prime[j] = false; 
      } 
  }
  sum[1] = 0; 
  sum[2] = 2;
  for(int i = 3; i < MM; i++) {
    if(prime[i]) sum[i] = i + sum[i-1];
    else sum[i] = sum[i-1];
  }
} 

int main () {
  sieve();
  cin >> Q;
  for(int i = 0; i < Q; i++) {
    cin >> a >> b;
    cout << sum[b] - sum[a-1] << "\n";
  }
}