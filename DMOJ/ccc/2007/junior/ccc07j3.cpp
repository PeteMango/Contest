#include <bits/stdc++.h>
using namespace std;

const int M[10] = {100,500,1000,5000,10000,25000,50000,100000,500000,1000000};
int N, Q, O, S = 1691600;

int main () {
  cin >> N;
  for(int i = 1; i <= N; i++) {
    cin >> Q;
    S -= M[Q-1];
  }
  cin >> O;
  if(O*(10-N) > S) cout << "deal" << endl;
  else cout << "no deal" << endl;
}