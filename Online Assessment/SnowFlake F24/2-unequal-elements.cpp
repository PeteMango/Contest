/*
2. Unequal Elements 13/15
*/

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'findMaxLength' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY skills
 *  2. INTEGER k
 */

int findMaxLength(vector<int> skills, int k) {
  int n = skills.size();

  vector<vector<int>> dp(n, vector<int>(k + 1, 0));
  int maxLen = 1;

  for (int i = 0; i < n; i++) {
    dp[i][0] = 1;
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j <= k; j++) {
      for (int p = 0; p < i; p++) {
        if (skills[p] == skills[i]) {
          dp[i][j] = max(dp[i][j], dp[p][j] + 1);
        } else {
          if (j > 0) {
            dp[i][j] = max(dp[i][j], dp[p][j - 1] + 1);
          }
        }
      }
      maxLen = max(maxLen, dp[i][j]);
    }
  }

  // cout << "dp is: \n";
  // for(int i = 0; i < n; i++) {
  //     for(int j = 0; j <= k; j++) {
  //         cout << dp[i][k] << " ";
  //     }
  //     cout << "\n";
  // }

  return maxLen;
}

int main() {
  ofstream fout(getenv("OUTPUT_PATH"));

  string skills_count_temp;
  getline(cin, skills_count_temp);

  int skills_count = stoi(ltrim(rtrim(skills_count_temp)));

  vector<int> skills(skills_count);

  for (int i = 0; i < skills_count; i++) {
    string skills_item_temp;
    getline(cin, skills_item_temp);

    int skills_item = stoi(ltrim(rtrim(skills_item_temp)));

    skills[i] = skills_item;
  }

  string k_temp;
  getline(cin, k_temp);

  int k = stoi(ltrim(rtrim(k_temp)));

  int result = findMaxLength(skills, k);

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
