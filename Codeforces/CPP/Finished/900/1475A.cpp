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
        long long n;
        cin >> n;
        while (n > 1) {
            if (n % 2 != 0) {
                break;
            }
            n /= 2;
        }
        if (n == 1) {
            cout << "NO" << endl;
        }
        else {
            cout << "YES" << endl;
        }
    }
}