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
        if(s.length() % 2 == 0) {
            int left = 0;
            int right = s.length() / 2;
            bool square = true;
            while(left < s.length() / 2 && right < s.length()) {
                if(s.at(left) != s.at(right)) {
                    square = false;
                    left = right;
                }
                else {
                    left++;
                    right++;
                }
            }
            if(square) {
                cout << "YES" << endl;
            }
            else {
                cout << "NO" << endl;
            }
        }
        else {
            cout << "NO" << endl;
        }
    }
    return 0;
}