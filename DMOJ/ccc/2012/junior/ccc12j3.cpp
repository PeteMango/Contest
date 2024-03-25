#include <bits/stdc++.h>
using namespace std;

char A[3][3];
char B[75][75];
int k;
int main() {
	cin >> k;
	A[0][0] = '*';
	A[0][1] = 'x';
	A[0][2] = '*';
	A[1][0] = ' ';
	A[1][1] = 'x';
	A[1][2] = 'x';
	A[2][0] = '*';
	A[2][1] = ' ';
	A[2][2] = '*';
	for(int i=0; i<3; i++) {
		for(int j=0; j<3; j++) {
			for(int l=0; l<k; l++) {
				for(int m=0; m<k; m++) {
					B[k*i+l][k*j+m] = A[i][j];
				}
			}
		}
	}
	for(int i=0; i<3*k; i++) {
		for(int j=0; j<3*k; j++) {
			cout << B[i][j];
		}
		cout << endl;
	}
}