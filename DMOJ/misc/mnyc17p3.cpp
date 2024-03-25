#include <bits/stdc++.h>
using namespace std;

const int MAXN = 10000005;
long long base = 131, Hsh1[MAXN], Hsh2[MAXN], Pow[MAXN];
int ans;
string a, b;

long long getSubHash (long long Hash[], long long Pow[], int L, int R) {
    return Hash[R] - Hash[L - 1] * Pow[R - L + 1];
}

int main () {
    cin >> a >> b;
    Pow[0] = 1;
    for(int i = 1; i <= a.length(); i++) {
        Hsh1[i] = Hsh1[i - 1] * base + a[i - 1];
        Pow[i] = Pow[i - 1] * base;
    }
    for(int i = 1; i<= b.length(); i++) {
        Hsh2[i] = Hsh2[i - 1] * base + b[i - 1];
    }
    for(int i = 1; i <= min(a.length(), b.length()); i++) {
        long long t1 = getSubHash(Hsh1, Pow, a.length() - i + 1, a.length()), t2 = getSubHash(Hsh2, Pow, 1, i);
        if(t1 == t2) {
            ans = i;
        }
    }
    cout << a << b.substr(ans, b.length()) << endl;
}
