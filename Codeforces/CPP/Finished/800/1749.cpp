#include <bits/stdc++.h>

using namespace std;

int main()
{
    int tests;
    cin >> tests;
    for(int i = 0; i < tests; i++) {
        int n;
        int m;
        cin >> n;
        cin >> m;
        for(int j = 0; j < m; j++) {
            int x;
            int y;
            cin >> x;
            cin >> y;
        }
        if(m >= n) {
            cout << "NO \n";
        }
        else {
            cout << "YES \n";
        }
    }
}