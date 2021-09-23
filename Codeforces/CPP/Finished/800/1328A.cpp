#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int a, b;
        cin >> a >> b;
        int answer = 0;
        while (true) {
            if (a % b == 0) {
                cout << answer << '\n';
                break;
            }
            else {
                if(a > b) {
                    cout << a % b << '\n';
                }
                else {
                    cout << b - a % b << '\n';
                }
                break;
            }
        }
    }
}