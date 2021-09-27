#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int i = 0; i < t; i++) {
        int n;
        cin >> n;
        if(n % 4 != 0) {
            cout << "NO" << '\n';
        }
        else {
            cout << "YES" << '\n';
            int remainder = (n + 2) * (n / 4);
            for(int j = 0; j < n / 2; j++) {
                cout << (j + 1) * 2 << " ";
            }
            for(int j = 0; j < (n / 2) - 1; j++) {
                cout << (j * 2) + 1 << " ";
                remainder -= (j * 2) + 1;
            }
            cout << remainder << '\n';
        }
    }
}