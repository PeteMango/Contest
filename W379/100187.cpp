#include <bits/stdc++.h>
using namespace std;

int minMovesToCaptureTheQueen(int a, int b, int c, int d, int e, int f)
{
    /*
    (a, b) - rook
    (c, d) - bishop
    (e, f) - queen
    */

    // cout << "(" << a << " " << b << ")\n";
    // cout << "(" << c << " " << d << ")\n";
    // cout << "(" << e << " " << f << ")\n";

    int minRook = 0, minBishop = 0;
    if (a == e)
    {
        // cout << "in 1\n";
        minRook = 1;
        if (a == c && ((b < d && d < f) || (b > d && d > f)))
        {
            minRook++;
        }
    }
    else if (b == f)
    {
        // cout << "in 2\n";
        minRook = 1;
        if (b == d && ((a < c && c < e) || (a > c && c > e)))
        {
            minRook++;
        }
    }
    else
    {
        minRook = 2;
    }

    if (abs(e - c) == abs(f - d))
    {
        minBishop = 1;
        if (e > c && f > d) // bottom left of queen
        {
            // cout << "was here1\n";
            if (a > c && e > a && b > d && f > b && abs(a - c) == abs(b - d))
            {
                minBishop++;
            }
        }
        if (e > c && f < d) // top left of queen
        {
            // cout << "was here2\n";
            if (a > c && e > a && b < d && f < b && abs(a - c) == abs(d - b))
            {
                minBishop++;
            }
        }
        if (e < c && f > d) // bottom right
        {
            // cout << "was here3\n";
            if (e < a && a < c && b > d && f > b && abs(c - a) == abs(b - d))
            {
                minBishop++;
            }
        }
        if (e < c && f < d) // top right
        {
            // cout << "was here4\n";
            if (a < c && e < a && b < d && f < b && abs(c - a) == abs(d - b))
            {
                minBishop++;
            }
        }
    }
    else if (abs((e - c) - (f - d)) % 2 == 0)
    {
        minBishop = 2;
    }
    else
    {
        minBishop = 10;
    }

    return min(minRook, minBishop);
}

int main()
{
    int a = 4, b = 7, c = 8, d = 3, e = 7, f = 4;
    int a1 = 7, b1 = 8, c1 = 7, d1 = 7, e1 = 7, f1 = 3;
    int a2 = 1, b2 = 1, c2 = 1, d2 = 4, e2 = 1, f2 = 8;
    cout << minMovesToCaptureTheQueen(a1, b1, c1, d1, e1, f1) << "\n";
}