#include <bits/stdc++.h>
using namespace std;

const int MAXN = 15;
int N, I;
string s[MAXN], ipt;

int main () {
    getline(cin, ipt);
    N = stoi(ipt);
    for(int i = 1; i <= N; i++) {
        getline(cin, s[i]);
    }
    for(int i = 1; i <= N; i++) {
        if(s[i].compare("Bessarion") == 0) {
            I = i;
            break;
        }
    }
    if(I == 1 || I == N) {
        cout << "N" << endl;
    }
    else if((s[I - 1].compare("Bayview") == 0 && s[I + 1].compare("Leslie") == 0) || (s[I - 1].compare("Leslie") == 0 && s[I + 1].compare("Bayview") == 0)) {
        cout << "Y" << endl;
    }
    else {
        cout << "N" << endl;
    }
}
