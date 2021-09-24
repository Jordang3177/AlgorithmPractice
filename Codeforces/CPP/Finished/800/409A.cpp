#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int i = 0; i < t; i++) {
        int a, b;
        cin >> a >> b;
        int answer = 0;
        a = abs(a - b);
        if (a == 0) {
            cout << answer << '\n';
        }
        else {
            answer += a / 10;
            a %= 10;
            if(a != 0) {
                answer += 1;
            }
            cout << answer << '\n';
        }
    }
}