#include <bits/stdc++.h>

using namespace std;

#define endl "\n"

int main()
{
    int t;
    cin >> t;
    for(int i = 0; i < t; i++) {
        int total;
        cin >> total;
        int a = total / 3;
        int b = total / 3;
        if(total % 3 == 1) {
            a += 1;
        }
        else if(total % 3 == 2) {
            b += 1;
        }
        cout << a << " " << b << endl;
    }
    return 0;
}