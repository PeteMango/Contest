#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 5;
int N, base = 131, ans;
long long P[MAXN] = {1}, Pre, Suf;
unordered_map<long long, int> mp;
string s;

int main () {
    cin >> N;
    for(int i = 1; i < MAXN; i++) {
        P[i] = P[i - 1] * base;
    }
    for(int i = 1; i <= N; i++) {
        cin >> s;
        Pre = Suf = 0;
        int Bst = 0;
        for(int j = 0; j < s.size(); j++) {
            Pre = Pre * base + s[j];
            Suf = Suf + s[s.size()-j-1] * P[j];
            if(Pre == Suf) {
                Bst = max(Bst, mp[Pre]);
            }
        }
        ans = max(ans, Bst + 1);
        mp[Pre] = Bst + 1;
    }
    cout << ans << "\n";
}
