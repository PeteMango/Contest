#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

typedef long ll;

ll sum_of_multiples(ll n, ll k) {
    ll m = (n - 1) / k;
    return (ll)(k * m * (m + 1) / 2);
}

ll func(int n) {
    if(n < 3) return 0L;
    return sum_of_multiples(n, 3) + sum_of_multiples(n, 5) - sum_of_multiples(n, 15);
}

int main()
{
    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string n_temp;
        getline(cin, n_temp);

        int n = stoi(ltrim(rtrim(n_temp)));

        cout << func(n) << "\n";
    }

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
