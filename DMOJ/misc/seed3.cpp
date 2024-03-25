#include <bits/stdc++.h>
using namespace std;

int I, N, J, arr[100005], diff[100005];

void update(int l, int r, int val){
    diff[l] += val;
    diff[r + 1] -= val;
}
int main(){
    cin >> I >> N >> J;
    for(int i = 0, a, b, k; i < J; i++){
        cin >> a >> b >> k;
        update(a, b, k);
    }
    for(int i = 1; i <= I; i++){
        if(i == 1) arr[i] = diff[i];
        else arr[i] = diff[i] + arr[i - 1];
    }
    int cnt = 0;
    for(int i = 1; i <= I; i++){
        if(arr[i] < N){
            cnt++;
        }
    }
    cout << cnt << endl;
}
