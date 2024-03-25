#include <bits/stdc++.h>
using namespace std;
#define pb push_back
const int MM = 1e5+5;
struct itm {
  string s;
  int p, q;
};
bool comparator (itm a, itm b) {
  return a.p < b.p;
}

int T, N, M, K, tot=0, price, quantityAvaliable, quantityPurchase;
string nameItem, namePurchase;
vector<itm> avaliableItems;
int main() {
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cin >> N;
    avaliableItems.clear();
    for(int j = 1; j <= N; j++) {
      cin >> M;
      for(int k = 1; k <= M; k++) {
        cin >> nameItem >> price >> quantityAvaliable;
        avaliableItems.pb({nameItem, price, quantityAvaliable});
      }
    }
    sort(avaliableItems.begin(), avaliableItems.end(), comparator);
    cin >> K;
    tot=0;
    for(int j = 1; j <= K; j++) {
      cin >> namePurchase >> quantityPurchase;
      for(int k = 0; k < avaliableItems.size(); k++) {
        if(quantityPurchase == 0) {
          break;
        }
        if(namePurchase == avaliableItems[k].s && quantityPurchase > 0) {
          if(avaliableItems[k].q >= quantityPurchase) {
            tot += avaliableItems[k].p * quantityPurchase;
            quantityPurchase=0;
            break;
          }
          else {
            tot += avaliableItems[k].p * avaliableItems[k].q;
            quantityPurchase -= avaliableItems[k].q;
          }
        }
      }
    }
    cout << tot << "\n";
  }
}