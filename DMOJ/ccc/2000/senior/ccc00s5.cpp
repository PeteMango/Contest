#include <bits/stdc++.h>

using namespace std;

int a[105], N;
double x[105], y[105];
int main() {
    scanf("%d", &N);
    for(int i = 1; i <= N; i++){
      scanf("%lf %lf", &x[i], &y[i]);
    }
    for(double xcord = 0.00; xcord <= 1000.00; xcord += 0.01){
      double best = 1000000005;
      vector<int> sheep;
      for(int i = 1; i <= N; i++){
        double dist = sqrt(y[i]*y[i] + (x[i] - xcord)*(x[i]-xcord));
        if(dist < best){
          sheep.clear();
          best = dist;
          sheep.push_back(i);
        }
        else if(dist == best){
          sheep.push_back(i);
        }
      }
      for(int i : sheep) a[i] = 1;
    }
    for(int i = 1; i <= N; i++){
      if(a[i] == 1){
        printf("The sheep at (%.2lf, %.2lf) might be eaten.\n",x[i],y[i]);
      }
    }
}