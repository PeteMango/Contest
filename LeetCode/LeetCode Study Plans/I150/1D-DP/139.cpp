#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  bool wordBreak(string s, vector<string> &wordDict) {
    function<bool(string)> breakable = [&](string s) -> bool {
      if (inDictionary(s, wordDict)) {
        return true;
      }
      int n = s.length();
      bool success = false;
      for (int i = 0; i < wordDict.size(); i++) {
        int m = wordDict[i].length();
        if (n >= m && s.substr(n - m, n) == wordDict[i]) {
          success |= breakable(s.substr(0, n - m));
          if (success) {
            return true;
          }
        }
      }
      return success;
    };

    function<bool()> breakable_tabulation = [&]() -> bool {
      if (inDictionary(s, wordDict)) {
        return true;
      }

      int n = s.length();
      vector<bool> dp(n, false);

      for (int i = 0; i < wordDict.size(); i++) {
        if (s.substr(0, wordDict[i].size()) == wordDict[i]) {
          dp[wordDict[i].size()] = true;
        }
      }

      for (int i = 0; i <= n; i++) {
        for (int j = 0; j < wordDict.size(); j++) {
          int m = wordDict[j].length();
          if (i < m) {
            continue;
          }
          cout << "m is: " << m << "\n"
               << "substr is: " << s.substr(i - m, m) << "\n";
          if (dp[i - m] && (s.substr(i - m, m) == wordDict[j])) {
            dp[i] = true;
            break;
          }
        }
      }
      return dp[n];
    };

    return breakable_tabulation();
  }

  bool inDictionary(string s, vector<string> &wordDict) {
    for (int i = 0; i < wordDict.size(); i++) {
      if (wordDict[i] == s) {
        return true;
      }
    }
    return false;
  }
};

int main() {
  Solution s;
  // string str = "leetcode";
  // vector<string> wordDict = {"leet", "code"};

  // string str = "applepenapple";
  // vector<string> wordDict = {"apple", "pen"};

  // string str = "catsandog";
  // vector<string> wordDict = {"cats", "dog", "sand", "and", "cat"};

  string str = "aaaaaaa";
  vector<string> wordDict = {"aaaa", "aa"};

  if (s.wordBreak(str, wordDict)) {
    cout << "true\n";
  } else {
    cout << "false\n";
  }
}
