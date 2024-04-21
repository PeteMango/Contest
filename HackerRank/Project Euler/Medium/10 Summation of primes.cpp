#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

typedef long ll;

vector<bool> sieve(1e6 + 5, true);
vector<ll> psa(1e6 + 5, 0);

void buildSieve(int N) {
    for(int i = 2; i < sqrt(N); i++) {
        if(sieve[i]) {
            for(int j = i*i; j < N; j += i) {
                sieve[j] = false;
            }
        }
    }
    for(int i = 2; i < N; i++) {
        if(sieve[i]) {
            psa[i] = psa[i-1] + i;
        }
        else {
            psa[i] = psa[i-1];
        }a
    }
}

ll func(int N) {
    return psa[N];
}

int main()
{
    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    buildSieve(1e6 + 5);

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
