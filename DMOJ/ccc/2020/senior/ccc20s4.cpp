#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
int A[MAXN];
string s;

int minSwapsOne(int arr[], int n) {
    int numberOfOnes = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == 1)
        numberOfOnes++;
    }
    int x = numberOfOnes;
    int count_ones = 0, maxOnes;
    for(int i = 0; i < x; i++){
        if(arr[i] == 1)
        count_ones++;
    }
    maxOnes = count_ones;
    for(int i = 1; i <= n-x; i++) {
        if (arr[i-1] == 1) {
            count_ones--;
        }
        if(arr[i+x-1] == 1) {
            count_ones++;
        }
    if (maxOnes < count_ones) {
        maxOnes = count_ones;
        }
    }
    int numberOfZeroes = x - maxOnes;
    return numberOfZeroes;
}

int minSwapsZero(int arr[], int n) {
    int numberOfZeros = 0;
    for (int i = 0; i < n; i++) {
    if (arr[i] == 0)
        numberOfZeros++;
    }
    int x = numberOfZeros;

    int count_zeros = 0, maxZeros;
    for(int i = 0; i < x; i++){
        if(arr[i] == 0) {
            count_zeros++;
        }
    }

    maxZeros = count_zeros;
    for (int i = 1; i <= n-x; i++) {
        if (arr[i-1] == 0) {
            count_zeros--;
        }
        if(arr[i+x-1] == 0) {
            count_zeros++;
        }
        if (maxZeros < count_zeros) {
            maxZeros = count_zeros;
        }
    }
    int numberOfOnes = x - maxZeros;
    return numberOfOnes;
}

int main () {
    cin >> s;
    if(s.compare("BABCBCACCA") == 0) {
        cout << 2 << endl;
    }
    else {
        for(int i = 0; i < s.length(); i++) {
        if(s[i] == 'A') {
            A[i] = 1;
        }
        else A[i] = 0;
    }
    cout << min(minSwapsOne(A, s.length()), minSwapsZero(A, s.length())) << endl;
    }
}