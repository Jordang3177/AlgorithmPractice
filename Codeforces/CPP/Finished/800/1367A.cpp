#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int i = 0; i < t; i++) {
        string b;
        cin >> b;
        string answer;
        for(int j = 0; j < b.length() - 1; j += 2) {
            answer += b[j];
        }
        answer += b[b.length() - 1];
        cout << answer << '\n';
    }
}