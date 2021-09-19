#include <bits/stdc++.h>

using namespace std;

int main()
{
    string n, m;
    cin >> n >> m;
    string answer;
    for (int i = 0; i < n.length(); i++) {
        if(n[i] == m[i]) {
            answer += '0';
        }
        else {
            answer += '1';
        }
    }
    cout << answer;
}