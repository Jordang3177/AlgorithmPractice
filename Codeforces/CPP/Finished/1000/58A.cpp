#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s;
    cin >> s;
    string answer;
    for (int i = 0; i < s.length(); i++) {
        if(answer.length() == 0 && s[i] == 'h') {
            answer += s[i];
        }
        else if (answer.length() == 1 && s[i] == 'e') {
            answer += s[i];
        }
        else if (answer.length() == 2 && s[i] == 'l' || answer.length() == 3 && s[i] == 'l') {
            answer += s[i];
        }
        else if (answer.length() == 4 && s[i] == 'o'){
            answer += s[i];
        }
    }
    if (answer == "hello") {
        cout << "YES";
    }
    else {
        cout << "NO";
    }
}