#include <bits/stdc++.h>
using namespace std;

const int MM = 1e5 + 5;
int N, M, a[MM], b[MM];

int main() {
  srand((unsigned) time(0));
  for(int testcase = 0; testcase <= 9; testcase++) {
    
    ofstream myfile;
    myfile.open("Testcase " + to_string(testcase));

    N = (rand() % MM) + 1, M = (rand() % MM) + 1;
    for(int i = 1; i <= N; i++) {
      a[i] = (rand() % (2 * MM)) - MM + 1;
    }
    for(int i = 1; i <= M; i++) {
      b[i] = (rand() % N) + 1;
    }
    myfile << N << " " << M << "\n";
    for(int i = 1; i <= N; i++) myfile << a[i] << "\n";
    for(int i = 1; i <= M; i++) myfile << b[i] << "\n";
  }
}
