#include <bits/stdc++.h>
using namespace std;

int suM, A[10];

int main () {
  for(int i = 1; i <= 9; i++) {
    cin >> A[i];
    suM += A[i];
  }
  for(int i = 1; i <= 9; i++) {
    for(int j = i+1; j <= 9; j++) {
      if(suM - A[i] - A[j] == 100) {
        for(int k = 1; k <= 9; k++) {
          if(k != i && k != j) {
            cout << A[k] << "\n";
          }
        }
      }
    }
  }
}