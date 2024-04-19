/*
3. Minimum Segments 15/15
*/

#include <functional>
#include <bits/stdc++.h>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'minimumDivision' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER_ARRAY b
 *  3. INTEGER k
 */

struct interval {
  int start, end;

  interval(int s, int e) : start(s), end(e) {}
};

int minimumDivision(vector<int> a, vector<int> b, int k) {
  function<bool(interval, interval)> compIntervals =
      [&](const interval &a, const interval &b) -> bool {
    if (a.start == b.start) {
      return a.end < b.end;
    }
    return a.start < b.start;
  };

  vector<interval> intervals;
  for (int i = 0; i < a.size(); i++) {
    intervals.push_back(interval(a[i], b[i]));
  }

  sort(intervals.begin(), intervals.end(), compIntervals);

  vector<interval> merged;
  interval cur = intervals[0];
  for (int i = 1; i < intervals.size(); i++) {
    if (intervals[i].start <= cur.end) {
      cur.end = max(cur.end, intervals[i].end);
    } else {
      merged.push_back(cur);
      cur = intervals[i];
    }
  }
  merged.push_back(cur);

  // for(int i = 0; i < merged.size(); i++) {
  //     cout << merged[i].start << " " << merged[i].end << "\n";
  // }

  if (merged.size() == 1) {
    return merged.size();
  }

  int numMerged = 0, l = 0, r = 0;
  while (l <= r && r < merged.size()) {
    while (r < merged.size() && merged[r].start - merged[l].end <= k) {
      r += 1;
    }
    numMerged = max(numMerged, r - l - 1);
    // cout << l << " " << r << " " << numMerged << "\n";
    l += 1;
  }
  return merged.size() - numMerged;
}

int main() {
  ofstream fout(getenv("OUTPUT_PATH"));

  string a_count_temp;
  getline(cin, a_count_temp);

  int a_count = stoi(ltrim(rtrim(a_count_temp)));

  vector<int> a(a_count);

  for (int i = 0; i < a_count; i++) {
    string a_item_temp;
    getline(cin, a_item_temp);

    int a_item = stoi(ltrim(rtrim(a_item_temp)));

    a[i] = a_item;
  }

  string b_count_temp;
  getline(cin, b_count_temp);

  int b_count = stoi(ltrim(rtrim(b_count_temp)));

  vector<int> b(b_count);

  for (int i = 0; i < b_count; i++) {
    string b_item_temp;
    getline(cin, b_item_temp);

    int b_item = stoi(ltrim(rtrim(b_item_temp)));

    b[i] = b_item;
  }

  string k_temp;
  getline(cin, k_temp);

  int k = stoi(ltrim(rtrim(k_temp)));

  int result = minimumDivision(a, b, k);

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
