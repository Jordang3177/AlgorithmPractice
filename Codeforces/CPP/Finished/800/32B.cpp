#include <bits/stdc++.h>

using namespace std;

int main()
{
    string x;
    cin >> x;
    int i = 0;
    while(i < x.length()) {
        if(i == x.length() - 1) {
            cout << "0";
            i++;
        }
        else if(x[i] == '-' && x[i + 1] == '-') {
            cout << "2";
            i += 2;
        }
        else if(x[i] == '-' && x[i + 1] == '.') {
            cout << "1";
            i += 2;
        }
        else {
            cout << "0";
            i += 1;
        }
    }
    return 0;
}