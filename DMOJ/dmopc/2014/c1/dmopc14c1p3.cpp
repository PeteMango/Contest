#include <bits/stdc++.h>
using namespace std;

int N, M;
double sum = 0, t, cur;
vector<double> a;
int main(){
    cin >> N;
    for(int i = 0; i < N; i++){
        cin >> t;
        sum += t;
    }
    cin >> M;
    for(int i = 1; i <= M; i++){
        cin >> t;
        sum += t;
        cur = sum / (N + i);
        cout << cur << endl;
    }
}
