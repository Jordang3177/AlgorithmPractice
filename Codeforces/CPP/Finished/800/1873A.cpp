#include <iostream>

using namespace std;

#define endl "\n"

int main()
{
    int t;
    cin >> t;
    for(int i = 0; i < t; i++) {
        string s;
        cin >> s;
        bool possible = false;
        if(s.at(0) == 'a' || s.at(1) == 'b' || s.at(2) == 'c') {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }
    return 0;
}