#include <iostream>
#include <bits/stdc++.h>
using namespace std;

string word;
int main(){
    cin >> word;
    while (word != "halt"){
        int t = 0;
        for (int i = 0; i < word.length(); i++){
            int c =word[i], n;
            if (i == word.length()-1) n=96;
            else n=word[i+1];
            n-=97;
            c-=97;
            if (c<18) t+=(c%3)+1;
            else {
                if (c==18) t+=4;
                else if (c==19) t+=1;
                else if (c==20) t+=2;
                else if (c==21) t+=3;
                else if (c==22) t++;
                else if (c==23) t+=2;
                else if (c==24) t+=3;
                else if (c==25) t+=4;
            }
            if ((c >= 0)&&(c <= 2) && (n >= 0) && (n <= 2)) t += 2;
            else if ((c >= 3) && (c <= 5) && (n >= 3) && (n <= 5)) t+=2;
            else if ((c >= 6) && (c <= 8) && (n >= 6) &&(n <= 8)) t+=2;
            else if ((c >= 9) && (c <= 11) && (n >=9) &&(n <= 11)) t+=2;
            else if ((c >= 12) && (c <= 14) && (n >= 12) &&(n <= 14)) t+=2;
            else if ((c >= 15) && (c <= 18) &&(n >=15)&&(n <= 18)) t+=2;
            else if ((c >= 19) && (c <= 21) && (n >= 19) && (n <= 21)) t+=2;
            else if ((c >= 22)&& (c <= 25) && (n >=22) && (n <= 25)) t+=2;
        }
        cout<<t<<endl;
        cin>>word;
    }
    return (0);
}