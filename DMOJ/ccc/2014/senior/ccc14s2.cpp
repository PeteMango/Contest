#include <bits/stdc++.h>
using namespace std;
#define str string
const int MM = 35;
int N;
str a[MM], b[MM];

int main() {
  cin >> N;
  for(int i = 1; i <= N; i++) {
    cin >> a[i];
  }
  for(int i = 1; i <= N; i++) {
    cin >> b[i];
  }
  for(int i = 1; i <= N; i++) {
    if(a[i] == b[i]) {
      cout << "bad\n";
      return 0;
    }
    for (int j = i; j > 0; j--) {
			if (b[i] == a[j] && b[j] != a[i]) {
				cout << "bad\n";
				return 0;
			}
		}
  }
  cout << "good\n";
  return 0;
}
