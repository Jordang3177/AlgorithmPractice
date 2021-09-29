#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int i = 0; i < t; i++) {
        int c0 = 0;
        int c1 = 0;
        string game;
        cin >> game;
        for(int j = 0; j < game.length(); j++) {
            if(game[j] == '0') {
                c0 += 1;
            }
            else {
                c1 += 1;
            }
        }
        int answer = min(c0, c1);
        if(answer % 2 == 0) {
            cout << "NET" << '\n';
        }
        else {
            cout << "DA" << '\n';
        }
    }
}