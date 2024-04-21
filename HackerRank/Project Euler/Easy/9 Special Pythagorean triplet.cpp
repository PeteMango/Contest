#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

typedef long ll;

vector<tuple<int, int, int>> pyth;
set<int> squares;



void computePyth(int n) {
    for(int i = 1; i <= n; i++) {
        squares.insert(i*i);
    }

    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            int k = i*i + j*j;
            if(squares.find(k) != squares.end()) {
                pyth.push_back(make_tuple(i, j, (int)(sqrt(k))));
            }
        }
    }
}

int max(int a, int b) {
    return a > b ? a : b;
}

ll func(int n) {
    ll maxProduct = -1;
    for(auto t : pyth) {
        if(get<0>(t) + get<1>(t) + get<2>(t) == n) {
            maxProduct = max(maxProduct, get<0>(t)*get<1>(t)*get<2>(t));
        }
    }
    return maxProduct;
}


int main()
{
    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    computePyth(3005);

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
