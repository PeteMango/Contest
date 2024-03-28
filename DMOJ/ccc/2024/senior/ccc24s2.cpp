#include <iostream>
#include <set>
#include <vector>

using namespace std;

bool solve(string s) {
  vector<int> freq(26, 0);
  for (int i = 0; i < s.size(); i++) {
    freq[s[i] - 'a'] += 1;
  }
  set<char> hvy, lgt;
  for (int i = 0; i < 26; i++) {
    if (freq[i] == 1) {
      lgt.insert((char)(i + (int)('a')));
    } else if (freq[i] > 1) {
      hvy.insert((char)(i + (int)('a')));
    }
  }

  for (int i = 1; i < s.size(); i++) {
    if (hvy.find(s[i]) != hvy.end() && lgt.find(s[i - 1]) == lgt.end()) {
      return false;
    }
    if (lgt.find(s[i]) != lgt.end() && hvy.find(s[i - 1]) == hvy.end()) {
      return false;
    }
  }
  return true;
}

int main() {
  int T, N;
  cin >> T >> N;
  for (int i = 0; i < T; i++) {
    string s;
    cin >> s;
    if (solve(s)) {
      cout << "T\n";
    } else {
      cout << "F\n";
    }
  }
}
