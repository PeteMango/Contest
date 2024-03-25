#include <bits/stdc++.h>
using namespace std;

int a, b, c;

int main () {
  scanf("%d %d %d", &a, &b, &c);
  if(a+b==c) {
    cout << a << "+" << b << "=" << c << endl;
  }
  else if(a-b==c) {
    cout << a << "-" << b << "=" << c << endl;
  }
  else if(a*b==c) {
    cout << a << "*" << b << "=" << c << endl;
  }
  else if(a/b==c) {
    cout << a << "/" << b << "=" << c << endl;
  }
  else if(a==b+c) {
    cout << a << "=" << b << "+" << c << endl;
  }
  else if(a==b-c) {
    cout << a << "=" << b << "-" << c << endl;
  }
  else if(a==b*c) {
    cout << a << "=" << b << "*" << c << endl;
  }
  else if(a==b/c) {
    cout << a << "=" << b << "/" << c << endl;
  }
}