#include <bits/stdc++.h>
using namespace std;

const int MM = 105;
int N, idx=-1;
string name[MM];
double mx =-1, rating[MM];

int main() {
  scanf("%d", &N);
  for(int i = 1; i <= N; i++) {
    cin >> name[i] >> rating[i];
  }
  for(int i = 1; i <= N; i++) {
    if(rating[i] > mx) {
      mx = rating[i];
      idx=i;
    }
  }
  cout << name[idx] << "\n";
}