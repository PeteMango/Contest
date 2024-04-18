/*
1. String Patterns 1/13
*/

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'calculateWays' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER wordLen
 *  2. INTEGER maxVowels
 */

int calculateWays(int wordLen, int maxVowels) {
  int MOD = 1e9 + 7;
  if (maxVowels == 0) {
    return pow(21, wordLen);
  }
  const int c = 21, v = 5;

  vector<vector<vector<long long>>> dp(
      wordLen + 1,
      vector<vector<long long>>(maxVowels + 1, vector<long long>(2, 0)));

  for (int i = 1; i <= v; i++) {
    dp[1][1][1] = v;
  }
  dp[1][0][1] = c;

  for (int len = 2; len <= wordLen; len++) {
    for (int c = 1; c < maxVowels; c++) {
      if (c <= maxVowels) {
        dp[len][c + 1][1] = (dp[len - 1][c][0] * v) % MOD;
      }
      dp[len][0][1] = (dp[len][0][1] + (dp[len - 1][c][0] * c) % MOD) % MOD;
    }
    dp[len][0][1] = (dp[len][0][1] + (dp[len - 1][0][1] * c) % MOD) % MOD;
    dp[len][1][0] = (dp[len - 1][0][1] * v) % MOD;
  }

  long long ans = 0;
  for (int c = 1; c <= maxVowels; c++) {
    ans = (ans + dp[wordLen][c][0]) % MOD;
  }
  ans = (ans + dp[wordLen][0][1]) % MOD;
  return ans % MOD;
}

int main() {
  ofstream fout(getenv("OUTPUT_PATH"));

  string wordLen_temp;
  getline(cin, wordLen_temp);

  int wordLen = stoi(ltrim(rtrim(wordLen_temp)));

  string maxVowels_temp;
  getline(cin, maxVowels_temp);

  int maxVowels = stoi(ltrim(rtrim(maxVowels_temp)));

  int result = calculateWays(wordLen, maxVowels);

  fout << result << "\n";

  fout.close();

  return 0;
}

string ltrim(const string &str) {
  string s(str);

  s.erase(s.begin(),
          find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace))));

  return s;
}

string rtrim(const string &str) {
  string s(str);

  s.erase(
      find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
      s.end());

  return s;
}
