#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    int a = 0, b = 0, c = 0;
    for (int i = 0; i < t; i++) {
        int tempA, tempB, tempC;
        cin >> tempA >> tempB >> tempC;
        a += tempA;
        b += tempB;
        c += tempC;

    }
    if (a == 0 && b == 0 && c == 0) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }
}