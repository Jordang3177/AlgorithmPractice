#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s;
    cin >> s;
    if (s.length() == 1 && tolower(s[0]) == s[0]){
        s[0] = toupper(s[0]);
        cout << s;
    }
    else {
        bool change = true;
        for (int i = 1; i < s.length(); i++) {
            if(tolower(s[i]) == s[i]) {
                change = false;
                break;
            }
        }
        if (change) {
            if(s[0] == tolower(s[0])) {
                s[0] = toupper(s[0]);
            }
            else {
                s[0] = tolower(s[0]);
            }
            for (int i = 1; i < s.length(); i++) {
                s[i] = tolower(s[i]);
            }
            cout << s;
        }
        else {
            cout << s;
        }

    }
}