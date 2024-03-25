#include <bits/stdc++.h>
using namespace std;

#define pb push_back

const string encrypt = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
string ipt;
deque<char> dq;

int main () {
    cin >> ipt;
    for(int i = 0; i < ipt.length(); i++) {
        int idx;
        for(int j = 0; j < encrypt.length(); j++) {
            if(encrypt[j] == ipt[i]) {
                idx = j;
                break;
            }
        }
        idx += 9;
        idx %= encrypt.length();
        dq.pb(encrypt[idx]);
    }
    for(int i = 0; i < dq.size(); i++) {
        cout << dq[i];
    }
    cout << endl;
}
