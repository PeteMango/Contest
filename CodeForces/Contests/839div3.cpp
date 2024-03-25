#include <bits/stdc++.h>
using namespace std;
int T;
const int MM = 2e5 + 5;

int minNum (int a, int b) {
    return a<b? a:b;
}

int maxNum (int a, int b) {
    return a>b? a:b;
}

int ceil (int a, int b) {
    return (a + b) % 2 == 0 ? ((a + b) / 2) : ((a + b + 1) / 2);
}

int floor (int a, int b) {
    return (a + b) % 2 == 0 ? ((a + b) / 2) : ((a + b - 1) / 2);
}

void solve () {
    int n, min = 0, max = 1e9, arr[MM];
    bool isSorted = true;
    scanf("%d", &n);
    for(int i = 1; i <= n; i++) {
        cin >> arr[i];
        if(i > 1 && arr[i] < arr[i-1]) {
            isSorted = false;
        }
    }

    if(isSorted == true) {
        printf("0\n");
        return;
    }

    for(int i = 1; i < n; i++) {
        if(arr[i] == arr[i+1]) {
            continue;
        }
        if(arr[i] < arr[i+1]) {
            max = minNum (max, floor(arr[i], arr[i+1]));
        }
        if(arr[i] > arr[i+1]) {
            min = maxNum (min, ceil(arr[i], arr[i+1]));
        }

    }
    if(min <= max) {
        printf("%d\n", max);
    }
    else {
        printf("-1\n");
    }
}

int main () {
    scanf("%d", &T);
    while(T--) {
        solve();
    }
}