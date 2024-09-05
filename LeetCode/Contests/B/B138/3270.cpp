class Solution {
public:
    int generateKey(int num1, int num2, int num3) {
        string a = to_string(num1), b = to_string(num2), c = to_string(num3);
        while(a.size() < 4) {
            a = "0" + a;
        }
        while(b.size() < 4) {
            b = "0" + b;
        }
        while(c.size() < 4) {
            c = "0" + c;
        }
        int ret = 0;
        for(int i = 0; i < 4; i++) {
            ret += pow(10, 3-i) * (min(a[i]-'0', min(b[i]-'0', c[i]-'0')));
        }
        return ret;
    }
};