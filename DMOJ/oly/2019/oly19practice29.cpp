#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int x, y, z;
int main() {
  scanf("%d %d %d", &x, &y, &z);
  for(int i = x; i <= x*x*x; i+=x){
    if(i%y==z){
      cout << "YES" << endl;
      return 0;
    }
  }
  cout << "NO" << endl;
  return 0;
}