#include <bits/stdc++.h>
using namespace std;

const int T = 10;
char c;

int compute () {
  char c = getchar();
  if(c == '(') {
    char com = getchar();
    getchar();
    int a = compute();
    getchar();
    int b = compute();
    getchar();
    switch(com) {
      case '+': return a+b;
      case '-': return a-b;
      case '*': return a*b;
      case 'q': return a/b;
      case 'r': return a%b;
    }
  }
  else if(c >= '0' && c <= '9') {
    return c - '0';
  }
}

int main () {
  for(int i = 1; i <= T; i++) {
    int ans = compute();
    while((c = getchar()) != '\n' && (c != EOF));
    cout << ans << "\n";
  }
}