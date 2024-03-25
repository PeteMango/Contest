#include <bits/stdc++.h>
using namespace std;
const string ROWS[3][27] = {
		{"o.", "o.", "oo", "oo", "o.", "oo", "oo", "o.", ".o", ".o", "o.", "o.", "oo", "oo", "o.", "oo", "oo", "o.", ".o", ".o", "o.", "o.", ".o", "oo", "oo", "o."},
		{"..", "o.", "..", ".o", ".o", "o.", "oo", "oo", "o.", "oo", "..", "o.", "..", ".o", ".o", "o.", "oo", "oo", "o.", "oo", "..", "o.", "oo", "..", ".o", ".o"},
		{"..", "..", "..", "..", "..", "..", "..", "..", "..", "..", "o.", "o.", "o.", "o.", "o.", "o.", "o.", "o.", "o.", "o.", "oo", "oo", ".o", "oo", "oo", "oo"}
};

string s;
int main() {
  getline(cin, s);
  for (int i = 0; i < 3; i++) {
		for (int j = 0; j < s.length(); j++) {
			if (s[j] == ' ') {
			 cout << "..";
      }
			else {
        cout << ROWS[i][(int)(s[j] - 'A')].c_str();
      }
		}
		cout << "\n";
	}
}