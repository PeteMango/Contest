#include <bits/stdc++.h>

using namespace std;

const int MM = 1e6+5;
int N, M, Q, a[MM], ans;
vector <int> dis;

int main() { /// use cin
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N >> M >> Q;
    for (int i = 0; i < Q; i++){
        cin >> a[i];
    }
    sort(a, a + Q);
    for (int i = 1; i < Q; i++){
        if (a[i] - a[i-1] != 1){
            dis.push_back(a[i] - a[i-1] - 1);
        }
    }
    sort(dis.begin(), dis.end());
    if (M == 0){
        cout << 0 << "\n";
        return 0;
    }
    if (M >= dis.size()+1){
        cout << Q << "\n";
        return 0;
    }
    int t = dis.size()+1 - M;
    for (int i = 0; i < t; i++){
        ans += dis[i];
    }
    cout << Q + ans << "\n";
}
