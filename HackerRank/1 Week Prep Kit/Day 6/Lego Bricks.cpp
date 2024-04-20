#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'legoBlocks' function below.
 *
 * The function is expected to return a LONG LONG INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER m
 */

int legoBlocks(int n, int m) {
    const int MOD = 1000000007;
    vector<int> row_combinations = {1, 1, 2, 4};

    while (row_combinations.size() <= m) {
        int new_combination = 0;
        int limit = row_combinations.size() < 4 ? row_combinations.size() : 4;
        for (int i = 1; i <= limit; ++i) {
            new_combination += row_combinations[row_combinations.size() - i];
            new_combination %= MOD;
        }
        row_combinations.push_back(new_combination);
    }

    vector<long long> total(m + 1);
    for (int i = 0; i <= m; ++i) {
        total[i] = 1;
        for (int j = 0; j < n; j++) {
            total[i] = total[i] * row_combinations[i] % MOD;
        }
    }

    vector<long long> unstable(m + 1, 0);

    for (int i = 2; i <= m; ++i) {
        long long result = 0;
        for (int j = 1; j < i; ++j) {
            result += (total[j] - unstable[j] + MOD) % MOD * total[i - j] % MOD;
            result %= MOD;
        }
        unstable[i] = result;
    }

    return (total[m] - unstable[m] + MOD) % MOD;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string first_multiple_input_temp;
        getline(cin, first_multiple_input_temp);

        vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

        int n = stoi(first_multiple_input[0]);

        int m = stoi(first_multiple_input[1]);

        long long result = legoBlocks(n, m);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
