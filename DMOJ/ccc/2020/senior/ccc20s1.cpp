#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005, INF = 0x3f3f3f3f;
int N;
double T[MAXN], S[MAXN], mx = -INF;

vector< pair <double,double> > v;
int main () {
    cin >> N;
    for(int i = 0; i < N; i++) {
        cin >> T[i] >> S[i];
        v.push_back( make_pair(T[i], S[i]) );
    }
    sort(v.begin(), v.end());
    for(int i = 1; i < N; i++) {
        double speed = abs((v[i].second-v[i-1].second)/(v[i].first-v[i-1].first));
        if(speed > mx) {
            mx = speed;
        }
    }
    printf("%.5f\n", mx);
}