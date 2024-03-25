#include <bits/stdc++.h>
using namespace std;
int N, saw[50005], logs[50005];
long long cnt = 0;

int main(){
    cin >> N;
    for(int i = 1; i <= N; i++){
        cin >> saw[i];
    }
    for(int i = 1; i <= N; i++){
        cin >> logs[i];
    }

    sort(saw, (saw+sizeof(saw)/sizeof(saw[0])), greater<int>());
    sort(logs, (logs+sizeof(logs)/sizeof(logs[0])), greater<int>());

    for(int i = 0; i < N; i++){
        cnt += (saw[i] * logs[N - i - 1]);
    }
    cout << cnt << endl;
}
