#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int N, M;
int main() {
  scanf("%d %d", &N, &M);
  if(M <= N){
      cout << "Congratulations, you are within the speed limit!" << endl;
  }
  else if(M > N && M - N <= 20){
    cout << "You are speeding and your fine is $100." << endl;
  }
  else if(M - N >= 21 && M - N <= 30) {
    cout << "You are speeding and your fine is $270." << endl;
  }
  else if(M - N >= 31){
    cout << "You are speeding and your fine is $500." << endl;
  }
}