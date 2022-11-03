#include <bits/stdc++.h>

using namespace std;

#define endl "\n"

int main()
{
    int tests;
    cin >> tests;
    while(tests--) {
        int candies;
        cin >> candies;
        int ones = 0;
        int sum = 0;
        int count = 0;
        while(candies--) {
            int candy;
            cin >> candy;
            sum += candy;
            count++;
            if(candy == 1) {
                ones++;
            }
        }
        if(sum % 2 != 0) {
            cout << "NO" << endl;
        }
        else if(ones >= 2) {
            cout << "YES" << endl;
        }
        else if(count % 2 == 0) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }
    return 0;
}