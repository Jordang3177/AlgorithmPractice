#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    string s;
    cin >> s;
    set<char> alphabet;
    if(n < 26) {
        cout << "NO";
        return 0;
    }
    for(int i = 0; i < n; i++) {
        alphabet.insert(tolower(s[i]));
    }
    if(alphabet.size() == 26) {
        cout << "YES";
    }
    else{
        cout << "NO";
    }
}