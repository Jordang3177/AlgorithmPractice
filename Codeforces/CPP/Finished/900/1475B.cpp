#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <numeric>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        if (n < 2020) {
            cout << "NO" << endl;
        }
        else {
            int y = n % 2020;
            int x = ((n - y) / 2020) - y;
            if (x >= 0) {
                cout << "YES\n";
            }
            else {
                cout << "NO\n";
            }
        }
    }
}