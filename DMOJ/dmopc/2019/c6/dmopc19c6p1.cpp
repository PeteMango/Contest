#include <iostream>

using namespace std;

double x, y, x1, y1, x2, y2, x3, y3, x4, y4;

int main() {
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> x4 >> y4;
    if ((y2-y1)*(x4-x3) == (y4-y3)*(x2-x1)){
        if ((y2-y1)*(x3-x1) == (y3-y1)*(x2-x1)){
            cout << "coincident\n";
        }
        else {
            cout << "parallel\n";
        }
    }
    else {
        if (x1 == x2){
            x = x1; y = (y4-y3)/(x4-x3)*(x-x3) + y3;
        }
        else if (x3 == x4){
            x = x3; y = (y2-y1)/(x2-x1)*(x-x1) + y1;
        }
        else {
            x = ((y3-y1) + (x1*(y2-y1)/(x2-x1)) - ((y4-y3)/(x4-x3)*x3)) / ((y2-y1)/(x2-x1)-(y4-y3)/(x4-x3));
            y = (y2-y1)/(x2-x1)*(x-x1) + y1;
        }
        printf("%.6f %.6f\n", x, y);
    }
    return 0;
}